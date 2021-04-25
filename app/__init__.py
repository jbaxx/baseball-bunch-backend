from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth
from flask_marshmallow import Marshmallow
from flask_mysqldb import MySQL
from flask_pymongo import PyMongo

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from config import app_config

db = MySQL()
ma = Marshmallow()
mongo = PyMongo()
auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()
from .apis import api

def create_app(config_name):
    sentry_sdk.init(
        # pylint: disable=line-too-long
        dsn="https://02b618763aae46868469ff4fe9e62564@o560387.ingest.sentry.io/5695909",
        integrations=[FlaskIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        environment=config_name
    )

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(app_config[config_name])
    app_config[config_name].init_app(app)
    db.init_app(app)
    mongo.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    return app
