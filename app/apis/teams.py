from flask import make_response, jsonify, abort
from flask_restplus import Namespace, Resource
import MySQLdb.cursors

from .. import db

api = Namespace('teams', description= 'The teams')

@api.route('')
class Teams(Resource):
    def get(self):
        """
        Teams Franchise
        """
        try:
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        except Exception:
            abort(500)
        try:
            cursor.execute('select * from potluck limit 2')
        except Exception:
            abort(500)
        cuenta = cursor.fetchall()

        return make_response(jsonify(cuenta), 200)

