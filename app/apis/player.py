import urllib.parse
from flask import abort
from flask import jsonify
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields as rest_fields
from marshmallow import Schema
from marshmallow import fields
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db
from .. import mongo
from .. import token_auth


api = Namespace('api/player', description= 'The players')

def parse_url(url):
    return urllib.parse.unquote(url)


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



@api.route('/<player_id>')
@api.doc(params={'player_id': 'A player ID'})
class SinglePlayer(Resource):
    """
    Player based methods
    """
    @api.doc(security='Bearer Auth')
    @api.response(200, 'Success', player_model)  # Api documentation
    @api.response(400, 'Player not found')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
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




class Sazon:
    def __init__(self, **kwargs):
        self.AB = kwargs.get('AB', '')
        self.G = kwargs.get('G', '')
        self.H = kwargs.get('H', '')
        self.R = kwargs.get('R', '')
        self.Team = kwargs.get('Team', '')
        self.Year = kwargs.get('Year', '')

class Jugador:
    def __init__(self, **kwargs):
        self.FirstName = kwargs.get('FirstName', '')
        self.LastName = kwargs.get('LastName', '')
        temps = kwargs.get('Seasons', '')
        tempera = [Sazon(**tepe) for tepe in temps]
        self.Seasons = tempera
        self.Id = kwargs.get('Id', '')


class SeasonsSchema(Schema):
    AB = fields.String(data_key='ab')
    H = fields.String(data_key='h')
    G = fields.String(data_key='g')
    R = fields.String(data_key='r')
    Team = fields.String(data_key='team')
    Year = fields.String(data_key='year')

class JugadorSchema(Schema):
    FirstName = fields.String(data_key='first_name')
    LastName = fields.String(data_key='last_name')
    Id = fields.String(data_key='_id_')
    Seasons = fields.List(fields.Nested(SeasonsSchema), data_key='seasons')


temporada_model = api.model('TemporadaModel', {
    'ab': rest_fields.String,
    'h': rest_fields.String,
    'g': rest_fields.String,
    'r': rest_fields.String,
    'team': rest_fields.String,
    'year': rest_fields.String,
    })

jugador_model = api.model('JugadorModel', {
    'first_name': rest_fields.String,
    'last_name': rest_fields.String,
    '_id_': rest_fields.String,
    'seasons': rest_fields.List(rest_fields.Nested(temporada_model))
    })


@api.route('/<player_id>/stats')
@api.doc(params={'player_id': 'A player id'})
class NamedPlayerStats(Resource):
    """
    Player Stats Methods
    """
    @api.doc(security='Bearer Auth')
    @api.response(200, 'Success', jugador_model)  # Api documentation
    @api.response(400, 'Player could not be found')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @token_auth.login_required
    def get(self, player_id):
        """
        Get a player stats for all seasons
        """
        # scherma01
        # bauertr01

        player_id = parse_url(player_id)

        pred = mongo.db.Data.find({'Id': player_id})
        pred_list = []
        for p in pred:
            p.pop('_id')
            pred_list.append(p)

        if len(pred_list) == 0:
            abort(404, 'Player could not be found')

        theplayer = pred_list[0]
        theplayerObject = Jugador(**theplayer)
        player = JugadorSchema().dump(theplayerObject)
        return jsonify(player)
