from flask import make_response, jsonify, abort
from flask_restplus import Namespace, Resource
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db

api = Namespace('pitching', description= 'The pitching statistics')

@api.route('')
class Pitching(Resource):
    def get(self):
        """
        Lists all pitching statistics
        """
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('select * from pitching limit 5')
        except ProgrammingError:
            abort(500)
            return
        pitching = cursor.fetchall()

        return make_response(jsonify(pitching), 200)

    def post(self):
        """
        Adds a pitching statistic
        """
        return abort(501)

    def put(self):
        """
        Updates a pitching statistic
        """
        return abort(501)

    def delete(self):
        """
        Deletes a pitching statistic
        """
        return abort(501)
