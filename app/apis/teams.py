from flask import abort, make_response, jsonify
from flask_restplus import Namespace, Resource
from flask_mysqldb import MySQL
import MySQLdb.cursors

api = Namespace('teams', description= 'The teams')
# mysql = MySQL(api)


# api.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
# api.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
# api.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
# api.config['MYSQL_DB'] = os.getenv('MYSQL_DB')



@api.route('/')
class Teams(Resource):
    def get(self):
        """
        Teams Franchise
        """
        return {"team": "yankees"}
        # try:
        #     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # except Exception:
        #     abort(500)
        # try:
        #     cursor.execute('select * from potluck limit 2')
        # except Exception:
        #     abort(500)
        # cuenta = cursor.fetchall()

        # return make_response(jsonify(cuenta), 200)

