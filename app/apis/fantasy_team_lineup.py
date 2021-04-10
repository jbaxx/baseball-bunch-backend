import urllib.parse
from flask import abort
from flask import g
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
from .fantasy_team import FantasyTeamModel


# pylint: disable=line-too-long
api = Namespace('api/fantasy-team-lineup', description= 'The fantasy team players')


def parse_url(url):
    return urllib.parse.unquote(url)

# To add new field
# 1. Add it to the Object class
# 2. Add it to the ObjectSchema class
class FantasyTeamPlayer:
    def __init__(self, **kwargs):
        self.fantasyteamid = kwargs.get('fantasyteamid', '')
        self.playerid = kwargs.get('playerid', '')

# Marshmallow Schema
class FantasyTeamPlayerSchema(Schema):
    fantasyteamid = fields.String(required=True)
    playerid = fields.String(required=True)

# To add new field
# 1. Add it to the Object class
# 2. Add it to the ObjectSchema class
class FantasyTeamLineup:
    def __init__(self, **kwargs):
        self.pitcher = kwargs.get('pitcher', '')
        self.catcher = kwargs.get('catcher', '')
        self.first_base = kwargs.get('first_base', '')
        self.second_base = kwargs.get('second_base', '')
        self.third_base = kwargs.get('third_base', '')
        self.short_stop = kwargs.get('short_stop', '')
        self.left_fielder = kwargs.get('left_fielder', '')
        self.center_fielder = kwargs.get('center_fielder', '')
        self.right_fielder = kwargs.get('right_fielder', '')


# Marshmallow Schema
class FantasyTeamLineupSchema(Schema):
    pitcher = fields.String(required=True)
    catcher = fields.String(required=True)
    first_base = fields.String(required=True)
    second_base = fields.String(required=True)
    third_base = fields.String(required=True)
    short_stop = fields.String(required=True)
    left_fielder = fields.String(required=True)
    center_fielder = fields.String(required=True)
    right_fielder = fields.String(required=True)


# rest_plus schema
fantasy_team_lineup_model = api.model('FantasyTeamLineup', {
    'pitcher': rest_fields.String,
    'catcher': rest_fields.String,
    'first_base': rest_fields.String,
    'second_base': rest_fields.String,
    'third_base': rest_fields.String,
    'short_stop': rest_fields.String,
    'left_fielder': rest_fields.String,
    'center_fielder': rest_fields.String,
    'right_fielder': rest_fields.String,
    })

class FantasyTeamLineupModel:
    def __init__(self):
        # TODO: remove limits
        self.GET_ALL_QUERY = """
        SELECT
            *
        FROM
            fantasy_team_players

        LIMIT 100
        """

        self.GET_BY_ID_QUERY = """
        SELECT
            *
        FROM
            fantasy_team_players
        WHERE
            fantasyteamid = %(fantasyteamid)s
        """

        self.INSERT_FANTASY_TEAM_LINEUP_QUERY = """
        INSERT INTO fantasy_team_players (fantasyteamid, playerid) VALUES
        (%(fantasyteamid)s, %(pitcher)s),
        (%(fantasyteamid)s, %(catcher)s),
        (%(fantasyteamid)s, %(first_base)s),
        (%(fantasyteamid)s, %(second_base)s),
        (%(fantasyteamid)s, %(third_base)s),
        (%(fantasyteamid)s, %(short_stop)s),
        (%(fantasyteamid)s, %(left_fielder)s),
        (%(fantasyteamid)s, %(center_fielder)s),
        (%(fantasyteamid)s, %(right_fielder)s);
        """

        self.DELETE_FANTASY_TEAM_LINEUP_QUERY = """
        DELETE FROM
            fantasy_team_players
        WHERE
            fantasyteamid = %(fantasyteamid)s;
        """

    def get_by_team_id(self, team_id):
        query = self.GET_BY_ID_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query, {'fantasyteamid': team_id})
        except ProgrammingError as err:
            raise err
        fantasy_team_players = cursor.fetchall()
        fantasy_team_players_list = []
        for f in fantasy_team_players:
            fantasy_team_players_list.append(FantasyTeamPlayer(**f))
        fantasy_team_players = FantasyTeamPlayerSchema(many=True).dump(fantasy_team_players_list)
        return fantasy_team_players

    def insert_fantasy_team_lineup(self, fantasy_team_id, fantasy_team_lineup: FantasyTeamLineup):
        query = self.INSERT_FANTASY_TEAM_LINEUP_QUERY

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query,
                    {
                        'fantasyteamid': fantasy_team_id,
                        'pitcher': fantasy_team_lineup.pitcher,
                        'catcher': fantasy_team_lineup.catcher,
                        'first_base': fantasy_team_lineup.first_base,
                        'second_base': fantasy_team_lineup.second_base,
                        'third_base': fantasy_team_lineup.third_base,
                        'short_stop': fantasy_team_lineup.short_stop,
                        'left_fielder': fantasy_team_lineup.left_fielder,
                        'center_fielder': fantasy_team_lineup.center_fielder,
                        'right_fielder': fantasy_team_lineup.right_fielder,
                        })
            db.connection.commit()
        except ProgrammingError as err:
            raise err

    def update_fantasy_team_lineup(self, fantasy_team_id, fantasy_team_lineup: FantasyTeamLineup):
        query = self.DELETE_FANTASY_TEAM_LINEUP_QUERY

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query,
                    {
                        'fantasyteamid': fantasy_team_id,
                        })
            db.connection.commit()
        except ProgrammingError as err:
            raise err

        query = self.INSERT_FANTASY_TEAM_LINEUP_QUERY

        try:
            cursor.execute(query,
                    {
                        'fantasyteamid': fantasy_team_id,
                        'pitcher': fantasy_team_lineup.pitcher,
                        'catcher': fantasy_team_lineup.catcher,
                        'first_base': fantasy_team_lineup.first_base,
                        'second_base': fantasy_team_lineup.second_base,
                        'third_base': fantasy_team_lineup.third_base,
                        'short_stop': fantasy_team_lineup.short_stop,
                        'left_fielder': fantasy_team_lineup.left_fielder,
                        'center_fielder': fantasy_team_lineup.center_fielder,
                        'right_fielder': fantasy_team_lineup.right_fielder,
                        })
            db.connection.commit()
        except ProgrammingError as err:
            raise err

    def delete_fantasy_team_lineup(self, fantasy_team_id):
        query = self.DELETE_FANTASY_TEAM_LINEUP_QUERY

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query,
                    {
                        'fantasyteamid': fantasy_team_id,
                        })
            db.connection.commit()
        except ProgrammingError as err:
            raise err


@api.route('/<fantasy_team_id>')
@api.doc(params={'fantasy_team_id': 'A Fantasy Team ID'})
class NamedFantasyTeamLineup(Resource):
    """
    Fantasy Team Lineup based methods
    """
    @api.doc(security='Bearer Auth')
    @api.response(200, 'Success', fantasy_team_lineup_model)  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(404, 'Fantasy Team Lineup not found')  # Api documentation
    @api.response(409, 'Fantasy Team does not have lineup')  # Api documentation
    @token_auth.login_required
    def get(self, fantasy_team_id):
        """
        Get a fantasy team lineup by fantasy team id
        """
        user_id = g.user.get('userid')
        try:
            # pylint: disable=line-too-long
            fantasy_team = FantasyTeamModel().get_by_userid_teamid(user_id, fantasy_team_id)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            abort(404, 'Fantasy Team could not be found')

        try:
            # pylint: disable=line-too-long
            fantasy_team_lineup_result = FantasyTeamLineupModel().get_by_team_id(fantasy_team_id)
        except ProgrammingError:
            abort(500)


        if len(fantasy_team_lineup_result) == 0:
            abort(409, description='Fantasy Team does not have lineup')

        return fantasy_team_lineup_result

    @api.doc(security='Bearer Auth')
    @api.response(201, 'Fantasy Team Lineup created')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(404, 'Fantasy Team could not be found')  # Api documentation
    @api.response(409, 'Fantasy Team Lineup already exists')  # Api documentation
    @api.response(422, 'Wrong body schema')  # Api documentation
    @api.expect(fantasy_team_lineup_model, validate=True)
    @token_auth.login_required
    def post(self, fantasy_team_id):
        """
        Creates a Fantasy Team Lineup
        """
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400

        try:
            # Validate the data acquired conforms to the UserSchema (marsh)
            fantasy_team_lineup_data = FantasyTeamLineupSchema().load(json_data)
        except ValidationError as err:
            return err.messages, 422

        # Validate Fantasy Team exists for current user,
        # before executing any action
        user_id = g.user.get('userid')
        try:
            # pylint: disable=line-too-long
            fantasy_team = FantasyTeamModel().get_by_userid_teamid(user_id, fantasy_team_id)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            abort(404, 'Fantasy Team could not be found')


        # pylint: disable=line-too-long
        team_lineup_exists = FantasyTeamLineupModel().get_by_team_id(fantasy_team_id)
        if fantasy_team_id is None or fantasy_team_id == '':
            abort(422)
        if team_lineup_exists:
            abort(409, description='Fantasy Team Lineup already exists')

        fantasy_team_lineup = FantasyTeamLineup(
                pitcher = fantasy_team_lineup_data.get('pitcher'),
                catcher = fantasy_team_lineup_data.get('catcher'),
                first_base = fantasy_team_lineup_data.get('first_base'),
                second_base = fantasy_team_lineup_data.get('second_base'),
                third_base = fantasy_team_lineup_data.get('third_base'),
                short_stop = fantasy_team_lineup_data.get('short_stop'),
                left_fielder = fantasy_team_lineup_data.get('left_fielder'),
                center_fielder = fantasy_team_lineup_data.get('center_fielder'),
                right_fielder = fantasy_team_lineup_data.get('right_fielder'),
        )

        FantasyTeamLineupModel().insert_fantasy_team_lineup(fantasy_team_id, fantasy_team_lineup)

        return {'message': 'Fantasy Team Lineup created'}, 201

    @api.doc(security='Bearer Auth')
    @api.response(200, 'Fantasy Team Lineup updated')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(404, 'Fantasy Team could not be found')  # Api documentation
    @api.response(409, 'Fantasy Team does not have lineup')  # Api documentation
    @api.response(422, 'Wrong body schema')  # Api documentation
    @api.expect(fantasy_team_lineup_model, validate=True)
    @token_auth.login_required
    def put(self, fantasy_team_id):
        """
        Updates a Fantasy Team Lineup
        """
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400

        try:
            # Validate the data acquired conforms to the UserSchema (marsh)
            fantasy_team_lineup_data = FantasyTeamLineupSchema().load(json_data)
        except ValidationError as err:
            return err.messages, 422

        # Validate Fantasy Team exists for current user,
        # before executing any action
        user_id = g.user.get('userid')
        try:
            # pylint: disable=line-too-long
            fantasy_team = FantasyTeamModel().get_by_userid_teamid(user_id, fantasy_team_id)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            abort(404, 'Fantasy Team could not be found')


        # pylint: disable=line-too-long
        team_lineup_exists = FantasyTeamLineupModel().get_by_team_id(fantasy_team_id)
        if fantasy_team_id is None or fantasy_team_id == '':
            abort(422)
        if not team_lineup_exists:
            abort(409, description='Fantasy Team does not have lineup')

        fantasy_team_lineup = FantasyTeamLineup(
                pitcher = fantasy_team_lineup_data.get('pitcher'),
                catcher = fantasy_team_lineup_data.get('catcher'),
                first_base = fantasy_team_lineup_data.get('first_base'),
                second_base = fantasy_team_lineup_data.get('second_base'),
                third_base = fantasy_team_lineup_data.get('third_base'),
                short_stop = fantasy_team_lineup_data.get('short_stop'),
                left_fielder = fantasy_team_lineup_data.get('left_fielder'),
                center_fielder = fantasy_team_lineup_data.get('center_fielder'),
                right_fielder = fantasy_team_lineup_data.get('right_fielder'),
        )

        FantasyTeamLineupModel().update_fantasy_team_lineup(fantasy_team_id, fantasy_team_lineup)

        return {'message': 'Fantasy Team Lineup updated'}, 200

    @api.doc(security='Bearer Auth')
    @api.response(200, 'Fantasy Team Lineup deleted')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(404, 'Fantasy Team could not be found')  # Api documentation
    @api.response(409, 'Fantasy Team does not have lineup')  # Api documentation
    @api.response(422, 'Wrong body schema')  # Api documentation
    @token_auth.login_required
    def delete(self, fantasy_team_id):
        """
        Updates a Fantasy Team Lineup
        """

        # Validate Fantasy Team exists for current user,
        # before executing any action
        user_id = g.user.get('userid')
        try:
            # pylint: disable=line-too-long
            fantasy_team = FantasyTeamModel().get_by_userid_teamid(user_id, fantasy_team_id)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            abort(404, 'Fantasy Team could not be found')


        # pylint: disable=line-too-long
        team_lineup_exists = FantasyTeamLineupModel().get_by_team_id(fantasy_team_id)
        if fantasy_team_id is None or fantasy_team_id == '':
            abort(422)
        if not team_lineup_exists:
            abort(409, description='Fantasy Team does not have lineup')

        FantasyTeamLineupModel().delete_fantasy_team_lineup(fantasy_team_id)

        return {'message': 'Fantasy Team Lineup deleted'}, 200
