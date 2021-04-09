from flask import make_response, jsonify, abort, request
from flask_restplus import Namespace, Resource
from MySQLdb import ProgrammingError
import MySQLdb.cursors

from .. import db

api = Namespace('api/search', description='Search by player name')


@api.route('')
class Search(Resource):
    def get(self):
        """
        Lists all players matching the query
        """
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            name = request.args.get('name')
            if request.args.get('position'):
                position_clause = "AND pos.pos = '{position}'".format(position=request.args.get('position'))
            else:
                position_clause = ""
            query = """
            SELECT p.*, pos.pos AS position FROM players p
            LEFT OUTER JOIN vw_players_position pos
                ON p.playerid = pos.playerid
            WHERE LOWER(CONCAT(p.namefirst,' ',p.namelast)) LIKE LOWER('%{name}%')
            {position_clause}
            ORDER BY birthyear DESC
            LIMIT 10
            """.format(name=name, position_clause=position_clause)
            cursor.execute(query)
        except ProgrammingError:
            abort(500)
            return
        search_results = cursor.fetchall()

        return make_response(jsonify(search_results), 200)
