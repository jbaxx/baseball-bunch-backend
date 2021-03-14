from flask_restplus import Api

from .fantasy import api as ns1

api = Api(
        title='The Baseball Bunch - Fantasy Baseball Analysis Toolkit',
        version='1.0',
        description='Predict and improve your fantasy game'
        )
api.add_namespace(ns1)
