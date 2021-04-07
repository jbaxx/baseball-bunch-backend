from flask import abort
from flask import g
from flask import jsonify
from flask import make_response
from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields as rest_fields
from marshmallow import Schema
from marshmallow import ValidationError
from marshmallow import fields
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db
from .. import token_auth


api = Namespace('api/fantasy-team', description= 'The fantasy teams')



# To add new field
# 1. Add it to the Object class
# 2. Add it to the ObjectSchema class
class FantasyTeam:
    def __init__(self, **kwargs):
        self.fantasyteamid = kwargs.get('fantasyteamid', '')
        self.teamname = kwargs.get('teamname', '')
        self.userid = kwargs.get('userid', '')

# Marshmallow Schema
class FantasyTeamSchema(Schema):
    fantasyteamid = fields.String()
    teamname = fields.String(required=True)
    userid = fields.String()


# rest_plus schema
fantasy_team_model_post = api.model('FantasyTeamPost', {
    # 'fantasyteamid': rest_fields.String,
    'teamname': rest_fields.String,
    # 'userid': rest_fields.String,
    })

fantasy_team_model_get = api.model('FantasyTeamGet', {
    'fantasyteamid': rest_fields.String,
    'teamname': rest_fields.String,
    'userid': rest_fields.String,
    })


class FantasyTeamModel:
    def __init__(self):
        # TODO: remove limits
        self.GET_ALL_QUERY = """
        SELECT
            *
        FROM
            fantasy_team

        LIMIT 100
        """

        self.GET_BY_ID_QUERY = """
        SELECT
            *
        FROM
            fantasy_team
        WHERE
            userid = %(userid)s
        """

        self.GET_BY_USERID_TEAMID_QUERY = """
        SELECT
            *
        FROM
            fantasy_team
        WHERE
            userid = %(userid)s
        AND
            fantasyteamid = %(fantasyteamid)s
        """

        self.GET_BY_USERID_TEAMNAME_QUERY = """
        SELECT
            *
        FROM
            fantasy_team
        WHERE
            userid = %(userid)s
        AND
            teamname = %(teamname)s
        """

        self.DELETE_BY_USERID_TEAMNAME_QUERY = """
        DELETE FROM
            fantasy_team
        WHERE
            userid = %(userid)s
        AND
            teamname = %(teamname)s
        """

        self.UPDATE_BY_USERID_TEAMNAME_QUERY = """
        UPDATE
            fantasy_team
        SET
            teamname = %(new_teamname)s
        WHERE
            userid = %(userid)s
        AND
            teamname = %(teamname)s
        """

        self.INSERT_FANTASY_TEAM_QUERY = """
        INSERT INTO fantasy_team (teamname, userid) VALUES
        (%(teamname)s, %(userid)s);
        """

    def get_all(self):
        query = self.GET_ALL_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query)
        except ProgrammingError as err:
            raise err
        fantasy_teams = cursor.fetchall()
        return fantasy_teams

    def get_by_user_id(self, user_id):
        query = self.GET_BY_ID_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query, {'userid': user_id})
        except ProgrammingError as err:
            raise err
        fantasy_teams = cursor.fetchall()
        fantasy_teams_list = []
        for f in fantasy_teams:
            fantasy_teams_list.append(FantasyTeam(**f))
        fantasy_teams = FantasyTeamSchema(many=True).dump(fantasy_teams_list)
        return fantasy_teams

    def get_by_userid_teamid(self, user_id, fantasy_team_id):
        query = self.GET_BY_USERID_TEAMID_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            # pylint: disable=line-too-long
            cursor.execute(query, {'userid': user_id, 'fantasyteamid': fantasy_team_id})
        except ProgrammingError as err:
            raise err
        fantasy_team = cursor.fetchall()
        return fantasy_team

    def get_by_userid_teamname(self, user_id, fantasy_team_name):
        query = self.GET_BY_USERID_TEAMNAME_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            # pylint: disable=line-too-long
            cursor.execute(query, {'userid': user_id, 'teamname': fantasy_team_name})
        except ProgrammingError as err:
            raise err
        fantasy_team = cursor.fetchall()
        return fantasy_team

    def insert_fantasy_team(self, fantasy_team: FantasyTeam):
        query = self.INSERT_FANTASY_TEAM_QUERY

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query,
                    {
                        'teamname': fantasy_team.teamname,
                        'userid': fantasy_team.userid,
                        })
            db.connection.commit()
        except ProgrammingError as err:
            raise err

    def delete_fantasy_team(self, fantasy_team: FantasyTeam):
        query = self.DELETE_BY_USERID_TEAMNAME_QUERY

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query,
                    {
                        'teamname': fantasy_team.teamname,
                        'userid': fantasy_team.userid,
                        })
            db.connection.commit()
        except ProgrammingError as err:
            raise err

    def update_fantasy_team(self, fantasy_team: FantasyTeam, new_teamname):
        query = self.UPDATE_BY_USERID_TEAMNAME_QUERY

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query,
                    {
                        'teamname': fantasy_team.teamname,
                        'userid': fantasy_team.userid,
                        'new_teamname': new_teamname,
                        })
            db.connection.commit()
        except ProgrammingError as err:
            raise err


@api.route('')
class FullFantasyTeam(Resource):
    """
    Fantasy Team based methods
    """
    @api.doc(security='Bearer Auth')
    @api.response(200, 'Success', fantasy_team_model_get)  # Api documentation
    @api.response(400, 'Fantasy Team not found')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
    @token_auth.login_required
    def get(self):
        """
        Get all fantasy teams of the current logged user
        """
        user_id = g.user.get('userid')
        try:
            fantasy_team = FantasyTeamModel().get_by_user_id(user_id)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            return {'message': 'Fantasy Teams not found for the user'}, 404

        # From the cursor result:
        # 1. Create a FantasyTeam object
        # 2. Validate it with FantasyTeamSchema (marshmallow)
        # 3. The result can be filtered with help of the FantasyTeamSchema model
        # pylint: disable=line-too-long
        # fantasy_team_result = FantasyTeamSchema().dump(FantasyTeam(**fantasy_team))
        # return fantasy_team_result
        return make_response(jsonify(fantasy_team), 200)

    @api.doc(security='Bearer Auth')
    @api.response(201, 'Fantasy Team created')  # Api documentation
    @api.response(422, 'Wrong body schema')  # Api documentation
    @api.expect(fantasy_team_model_post, validate=True)
    @token_auth.login_required
    def post(self):
        """
        Creates a Fantasy Team
        """
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400

        try:
            # Validate the data acquired conforms to the UserSchema (marsh)
            fantasy_team_data = FantasyTeamSchema().load(json_data)
        except ValidationError as err:
            return err.messages, 422

        teamname = fantasy_team_data.get('teamname')

        user_id = g.user.get('userid')

        # pylint: disable=line-too-long
        teamname_exists = FantasyTeamModel().get_by_userid_teamname(user_id, teamname)
        if teamname is None or teamname == '':
            abort(422)
        if teamname_exists:
            abort(409, description='Team Name already exists')

        fantasy_team = FantasyTeam(
                teamname = fantasy_team_data.get('teamname'),
                userid = user_id,
        )

        FantasyTeamModel().insert_fantasy_team(fantasy_team)

        return {'message': 'a fantasy team created'}, 201


@api.route('/<fantasy_team_id>')
@api.doc(params={'fantasy_team_id': 'A Fantasy Team ID'})
class SingleFantasyTeam(Resource):
    """
    Fantasy Team based methods
    """
    @api.doc(security='Bearer Auth')
    @api.response(200, 'Success', fantasy_team_model_get)  # Api documentation
    @api.response(400, 'Fantasy Team not found')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
    @token_auth.login_required
    def get(self, fantasy_team_id):
        """
        Get a fantasy team by id
        """
        user_id = g.user.get('userid')
        try:
            # pylint: disable=line-too-long
            fantasy_team = FantasyTeamModel().get_by_userid_teamid(user_id, fantasy_team_id)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            return {'message': 'Fantasy Team could not be found'}, 404

        # From the cursor result:
        # 1. Create a FantasyTeam object
        # 2. Validate it with FantasyTeamSchema (marshmallow)
        # 3. The result can be filtered with help of the FantasyTeamSchema model
        # pylint: disable=line-too-long
        fantasy_team_result = FantasyTeamSchema().dump(FantasyTeam(**fantasy_team[0]))
        return fantasy_team_result


@api.route('/<fantasy_team_name>/name')
@api.doc(params={'fantasy_team_name': 'A Fantasy Team Name'})
class NamedFantasyTeam(Resource):
    """
    Fantasy Team based methods
    """
    @api.doc(security='Bearer Auth')
    @api.response(200, 'Success', fantasy_team_model_get)  # Api documentation
    @api.response(400, 'Fantasy Team not found')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
    @token_auth.login_required
    def get(self, fantasy_team_name):
        """
        Get a fantasy team by name
        """
        user_id = g.user.get('userid')
        try:
            # pylint: disable=line-too-long
            fantasy_team = FantasyTeamModel().get_by_userid_teamname(user_id, fantasy_team_name)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            return {'message': 'Fantasy Team could not be found'}, 404

        # From the cursor result:
        # 1. Create a FantasyTeam object
        # 2. Validate it with FantasyTeamSchema (marshmallow)
        # 3. The result can be filtered with help of the FantasyTeamSchema model
        # pylint: disable=line-too-long
        fantasy_team_result = FantasyTeamSchema().dump(FantasyTeam(**fantasy_team[0]))
        return fantasy_team_result

    @api.doc(security='Bearer Auth')
    @api.response(200, 'Team Deleted')  # Api documentation
    @api.response(400, 'Fantasy Team not found')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
    @token_auth.login_required
    def delete(self, fantasy_team_name):
        """
        Delete a fantasy team by name
        """
        user_id = g.user.get('userid')
        try:
            # pylint: disable=line-too-long
            fantasy_team = FantasyTeamModel().get_by_userid_teamname(user_id, fantasy_team_name)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            return {'message': 'Fantasy Team could not be found'}, 404

        print(fantasy_team)
        print(type(fantasy_team))
        print(type(fantasy_team[0]))

        fantasy_team_mod = FantasyTeam(
                teamname = fantasy_team[0].get('teamname'),
                userid = user_id,
        )

        try:
            # pylint: disable=line-too-long
            FantasyTeamModel().delete_fantasy_team(fantasy_team_mod)
        except ProgrammingError:
            abort(500)

        message = f'Fantasy Team {fantasy_team_name} has been deleted'
        return {'message': message}, 200


    @api.doc(security='Bearer Auth')
    @api.response(200, 'Team Updated')  # Api documentation
    @api.response(400, 'Fantasy Team not found')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(422, 'Wrong body schema')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
    @api.expect(fantasy_team_model_post, validate=True)
    @token_auth.login_required
    def put(self, fantasy_team_name):
        """
        Update a fantasy team attributes (found by name)
        """

        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400

        try:
            # Validate the data acquired conforms to the UserSchema (marsh)
            fantasy_team_data = FantasyTeamSchema().load(json_data)
        except ValidationError as err:
            return err.messages, 422

        new_teamname = fantasy_team_data.get('teamname')

        user_id = g.user.get('userid')
        try:
            # pylint: disable=line-too-long
            fantasy_team = FantasyTeamModel().get_by_userid_teamname(user_id, fantasy_team_name)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            return {'message': 'Fantasy Team could not be found'}, 404

        print(fantasy_team)
        print(type(fantasy_team))
        print(type(fantasy_team[0]))

        fantasy_team_mod = FantasyTeam(
                teamname = fantasy_team[0].get('teamname'),
                userid = user_id,
        )


        print(fantasy_team_mod)
        print(new_teamname)
        try:
            # pylint: disable=line-too-long
            FantasyTeamModel().update_fantasy_team(fantasy_team_mod, new_teamname)
        except ProgrammingError:
            abort(500)

        # pylint: disable=line-too-long
        message = f'Fantasy Team {fantasy_team_name} has been updated to {new_teamname}'
        return {'message': message}, 200
