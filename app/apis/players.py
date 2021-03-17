from flask import make_response, jsonify, abort
from flask_restplus import Namespace, Resource
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db

api = Namespace('players', description= 'The players')

@api.route('')
class Players(Resource):
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
