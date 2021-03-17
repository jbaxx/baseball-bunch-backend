
from flask import make_response, jsonify, abort
from flask_restplus import Namespace, Resource
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db

api = Namespace('teams-franchises', description= 'The teams franchises')

@api.route('')
class TeamsFranchises(Resource):
    def get(self):
        """
        Lists all teams franchises
        """
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('select * from teams_franchises limit 5')
        except ProgrammingError:
            abort(500)
            return
        teams_franchises = cursor.fetchall()

        return make_response(jsonify(teams_franchises), 200)

    def post(self):
        """
        Adds a team franchise
        """
        return abort(501)

    def put(self):
        """
        Updates a team franchise
        """
        return abort(501)

    def delete(self):
        """
        Deletes a team franchise
        """
        return abort(501)
