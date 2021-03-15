from flask import abort, make_response, jsonify
from flask_restplus import Namespace, Resource
from .. import db
import MySQLdb.cursors

api = Namespace('teams', description= 'The teams')

@api.route('')
class Teams(Resource):
    def get(self):
        """
        Teams Franchise
        """
        # return {"team": "yankees"}
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

