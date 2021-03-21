from flask import make_response, jsonify, abort, request
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields as rest_fields
from marshmallow import fields, ValidationError, Schema
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db

api = Namespace('players', description= 'The players')

@api.route('')
class Players(Resource):
    """
    Players
    """
    def get(self):
        """
        Lists all players
        """
        players = PlayerModel().get_all()
        return make_response(jsonify(players), 200)


class PlayerModel:
    def __init__(self, **kwargs):
        self.playerID = kwargs.get('playerID', '')
        self.birthYear = kwargs.get('birthYear', '')
        self.birthMonth = kwargs.get('birthMonth', '')
        self.birthDay = kwargs.get('birthDay', '')
        self.birthCountry = kwargs.get('birthCountry', '')
        self.birthState = kwargs.get('birthState', '')
        self.birthCity = kwargs.get('birthCity', '')
        self.query = ''

    def get_all(self):
        query = """
            SELECT
                *
            FROM
                players
            """
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query)
        except ProgrammingError as err:
            raise err
        players = cursor.fetchall()
        return players

    def get_by_id(self, player_id):
        query = """
            SELECT
              playerID,
              birthYear,
              birthMonth,
              birthDay,
              birthCountry,
              birthState,
              birthCity,
              debut
            FROM
                players
            WHERE
                playerID = %(player_id)s
            """
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query, {'player_id': player_id})
        except ProgrammingError as err:
            raise err
        player = cursor.fetchall()
        return player


class PlayerSchema(Schema):
    playerID = fields.String()
    birthYear = fields.String(required=True)
    birthMonth = fields.String(required=True)
    birthDay = fields.String(required=True)
    birthCountry = fields.String()
    birthState = fields.String()
    birthCity = fields.String()

player_model = api.model('Player', {
    'playerID': rest_fields.String,
    'birthYear': rest_fields.String,
    'birthMonth': rest_fields.String,
    'birthDay': rest_fields.String,
    'birthCountry': rest_fields.String,
    'birthState': rest_fields.String,
    'birthCity': rest_fields.String,
    })


@api.route('/<player_id>')
@api.doc(params={'player_id': 'A player ID'})
class Player(Resource):
    """
    Player based methods
    """
    @api.response(200, 'Success', player_model)  # Api documentation
    @api.response(400, 'Player not found')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
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

        return make_response(jsonify(player), 200)


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
            data = PlayerSchema().load(json_data)
        except ValidationError as err:
            return err.messages, 422

        return {'message': 'a player created'}, 201
