from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_mysqldb import MySQL
from flask_restplus import Api, Resource
from .apis import api
import MySQLdb.cursors
import os
import config

def create_app(config_name):
    app = Flask(__name__)
    api.init_app(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    return api
