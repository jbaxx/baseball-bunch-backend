from flask import make_response, jsonify, abort
from flask_restplus import Namespace, Resource
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db

api = Namespace('batting', description= 'The batting statistics')

@api.route('')
class Batting(Resource):
    def get(self):
        """
        Lists all batting statistics
        """
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('select * from batting limit 5')
        except ProgrammingError:
            abort(500)
            return
        batting = cursor.fetchall()

        return make_response(jsonify(batting), 200)

    def post(self):
        """
        Adds a batting statistic
        """
        return abort(501)

    def put(self):
        """
        Updates a batting statistic
        """
        return abort(501)

    def delete(self):
        """
        Deletes a batting statistic
        """
        return abort(501)
