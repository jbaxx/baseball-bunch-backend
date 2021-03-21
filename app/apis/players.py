from flask import make_response, jsonify, abort, request
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields as rest_fields
# from flask_marshmallow import fields, ValidationError
from marshmallow import fields, ValidationError
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db
from .. import ma

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
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('select * from players limit 5')
        except ProgrammingError:
            abort(500)
            return
        players = cursor.fetchall()

        return make_response(jsonify(players), 200)

    def post(self):
        """
        Adds a player
        """
        return abort(501)

    def put(self):
        """
        Updates a player
        """
        return abort(501)

    def delete(self):
        """
        Deletes a player
        """
        return abort(501)

model = api.model('Player', {
    'name': rest_fields.String,
    })

player_post = api.model('PlayerPost', {
    'first_name': rest_fields.String,
    'last_name': rest_fields.String,
    })

def return_santeno():
    return {'name': 'luis', 'type': 'pitcher', 'age': 27}

eljugador = api.model('ElJugador', {
    'name': rest_fields.String,
    'type': rest_fields.String,
    'age': rest_fields.Integer,
    })

class Jugador(rest_fields.Raw):
    def format(self, value):
        return {'name': value.name, 'age': value.age}

los_jugadores = []

class PlayerModel:
    def __init__(self, **kwargs):
                 # playerID,
                 # birthYear,
                 # birthMonth,
                 # birthDay,
                 # birthCountry,
                 # birthState,
                 # birthCity):
        self.playerID = kwargs['playerID']
        self.birthYear = kwargs['birthYear']
        self.birthMonth = kwargs['birthMonth']
        self.birthDay = kwargs['birthDay']
        self.birthCountry = kwargs['birthCountry']
        self.birthState = kwargs['birthState']
        self.birthCity = kwargs['birthCity']

class PlayerModelSchema(ma.Schema):
    playerID = fields.Str()
    birthYear = fields.Str()
    birthMonth = fields.Str()
    birthDay = fields.Str()
    birthCountry = fields.Str()
    birthState = fields.Str()
    birthCity = fields.Str()

player_model_schema = PlayerModelSchema()

# playerID 
# birthYear
# birthMonth
# birthDay
# birthCountry
# birthState
# birthCity
# deathYear
# deathMonth
# deathDay
# deathCountry
# deathState
# deathCity
# nameFirst
# nameLast
# nameGiven
# weight
# height
# bats
# throws
# debut
# finalGame
# retroID
# bbrefID

class PlayerSchema(ma.Schema):
    num = fields.Int()
    nombre = fields.Str()
    apellido = fields.Str()

player_schema = PlayerSchema()

@api.route('/<player_id>')
@api.doc(params={'player_id': 'An ID'})
class Player(Resource):
    """
    Player based methods
    """
    @api.response(200, 'Success', model)  # Api documentation
    @api.response(400, 'Player not found')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
    # @api.marshal_with(eljugador)
    def get(self, player_id):
        """
        Get a player by id
        """
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("""
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
                           """, {
                               'player_id': player_id
                               })
        except ProgrammingError:
            abort(500)
            return
        player = cursor.fetchall()
        if not player:
            return {'message': 'Player could not be found'}, 400
        print(player[0])
        p = PlayerModel(**player[0])
        player_result = player_model_schema.dump(p)

        # return player
        return player_result

        # return make_response(jsonify(player), 200)

        # return make_response(jsonify(return_santeno()), 200)
        # return return_santeno()

    # weberry01
    # @api.doc(model='ElJugador', body=Jugador)
    # @api.expect(player_post, validate=True)
    @api.expect(player_schema, validate=True)
    # @api.marshal_with(eljugador)
    def post(self, player_id):
        """
        Adds a player
        """
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400
        try:
            data = player_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422

        print(data)

        return {'message': 'a player created'}

        # print(api.payload)
        # return request.form
        # return api.payload
        # return request.get_json(force=True)
