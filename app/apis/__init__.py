from flask_restplus import Api

from .fantasy import api as ns1
from .players import api as ns2
from .teams import api as ns3

api = Api(
        title='The Baseball Bunch - Fantasy Baseball Analysis Toolkit',
        version='1.0',
        description='Predict and improve your fantasy game'
        )

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
