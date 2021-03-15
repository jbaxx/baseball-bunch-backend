from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import app_config

db = MySQL()

from .apis import api

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(app_config[config_name])
    app_config[config_name].init_app(app)
    db.init_app(app)
    api.init_app(app)

    return app
