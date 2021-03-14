from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_mysqldb import MySQL
from flask_restplus import Api, Resource
from apis import api
import MySQLdb.cursors
import os


app = Flask(__name__)
# api = Api(app)

# With Blueprint
# blueprint = Blueprint('api', __name__, url_prefix='/api')
# api = Api(blueprint, doc='/documentation') # , doc=False
# app.register_blueprint(blueprint)

# With Namespaces
api.init_app(app)


app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')


mysql = MySQL(app)

@api.route('/teams/')
class Teams(Resource):
    def get(self):
        """
        Teams
        """
        return make_response(jsonify({"teams": "braves"}), 200)

@api.route('/content')
class Content(Resource):
    def get(self):
        """
        Teams Franchise
        """
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        except Exception:
            abort(500)
        try:
            cursor.execute('select * from potluck limit 2')
        except Exception:
            abort(500)
        cuenta = cursor.fetchall()

        return make_response(jsonify(cuenta), 200)

