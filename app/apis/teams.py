from flask import make_response, jsonify, abort
from flask_restplus import Namespace, Resource
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db

api = Namespace('teams', description= 'The teams')

@api.route('')
class Teams(Resource):
    def get(self):
        """
        Lists all teams
        """
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('select * from teams limit 5')
        except ProgrammingError:
            abort(500)
            return
        teams = cursor.fetchall()

        return make_response(jsonify(teams), 200)

    def post(self):
        """
        Adds a team
        """
        return abort(501)

    def put(self):
        """
        Updates a team
        """
        return abort(501)

    def delete(self):
        """
        Deletes a team
        """
        return abort(501)
