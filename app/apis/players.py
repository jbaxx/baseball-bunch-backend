from flask import make_response, jsonify, abort, request
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields as rest_fields
from marshmallow import fields, ValidationError, Schema
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db
from .. import auth
from .. import token_auth


api = Namespace('players', description= 'The players')

@api.route('')
class AllPlayers(Resource):
    """
    Players
    """
    @api.doc(security='Basic Auth')
    @auth.login_required
    def get(self):
        """
        Lists all players
        """
        players = PlayerModel().get_all()
        return make_response(jsonify(players), 200)


# To add new field
# 1. Add it to the Object class
# 2. Add it to the ObjectSchema class
class Player:
    def __init__(self, **kwargs):
        self.playerid = kwargs.get('playerid', '')
        self.birthmonth = kwargs.get('birthmonth', '')
        self.birthyear = kwargs.get('birthyear', '')
        self.birthday = kwargs.get('birthday', '')
        self.namefirst = kwargs.get('namefirst', '')
        self.namelast = kwargs.get('namelast', '')
        self.bats = kwargs.get('bats', '')
        self.throws = kwargs.get('throws', '')
        self.currentteamid = kwargs.get('currentteamid', '')
        self.debut = kwargs.get('debut', '')
        self.final_game = kwargs.get('final_game', '')
        self.active = kwargs.get('active', '')


class PlayerModel:
    def __init__(self):
        # TODO: remove limits
        self.GET_ALL_QUERY = """
        SELECT
            *
        FROM
            players

        LIMIT 100
        """

        self.GET_BY_ID_QUERY = """
        SELECT
            *
        FROM
            players
        WHERE
            playerid = %(player_id)s
        """

    def get_all(self):
        query = self.GET_ALL_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query)
        except ProgrammingError as err:
            raise err
        players = cursor.fetchall()
        return players

    def get_by_id(self, player_id):
        query = self.GET_BY_ID_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query, {'player_id': player_id})
        except ProgrammingError as err:
            raise err
        player = cursor.fetchall()
        return player


# Marshmallow Schema
class PlayerSchema(Schema):
    playerid = fields.String(required=True)
    birthmonth = fields.String()
    birthyear = fields.String()
    birthday = fields.String()
    namefirst = fields.String()
    namelast = fields.String()
    bats = fields.String()
    throws = fields.String()
    currentteamid = fields.String()
    debut = fields.String()
    final_game = fields.String()
    active = fields.String()


# rest_plus schema
player_model = api.model('Player', {
    'playerid': rest_fields.String,
    'birthmonth': rest_fields.String,
    'birthyear': rest_fields.String,
    'birthday': rest_fields.String,
    'namefirst': rest_fields.String,
    'namelast': rest_fields.String,
    'bats': rest_fields.String,
    'throws': rest_fields.String,
    'currentteamid': rest_fields.String,
    'debut': rest_fields.String,
    'final_game': rest_fields.String,
    'active': rest_fields.String,
    })


@api.route('/<player_id>')
@api.doc(params={'player_id': 'A player ID'})
class SinglePlayer(Resource):
    """
    Player based methods
    """
    @api.response(200, 'Success', player_model)  # Api documentation
    @api.response(400, 'Player not found')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
    @token_auth.login_required
    def get(self, player_id):
        """
        Get a player by id
        """
        try:
            player = PlayerModel().get_by_id(player_id)
        except ProgrammingError:
            abort(500)

        if not player:
            return {'message': 'Player could not be found'}, 400

        # From the cursor result:
        # 1. Create a Player object
        # 2. Validate it with PlayerSchema (marshmallow)
        # 3. The result can be filtered with help of the PlayerSchema model
        player_result = PlayerSchema().dump(Player(**player[0]))
        return player_result

        # return make_response(jsonify(player_result), 200)


    @api.response(201, 'Player created')  # Api documentation
    @api.response(422, 'Wrong body schema')  # Api documentation
    @api.expect(player_model, validate=True)
    def post(self, player_id):
        """
        Adds a player
        """
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400

        try:
            # Validate the data acquired conforms to the PlayerSchema (marsh)
            data = PlayerSchema().load(json_data)
        except ValidationError as err:
            return err.messages, 422

        _ = player_id
        _ = data
        # TODO: add player

        return {'message': 'a player created'}, 201
