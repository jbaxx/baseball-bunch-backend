from flask_restplus import Api

from .batting import api as ns1
from .pitching import api as ns2
from .players import api as ns3
from .teams import api as ns4
from .teams_franchises import api as ns5

from .api_content import api as temp_ns6

authorizations = {
        'apiKey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-KEY',
            }
        }

api = Api(
        title='The Baseball Bunch - Fantasy Baseball Analysis Toolkit',
        version='1.0',
        description='Predict and improve your fantasy game',
        authorizations=authorizations,
        doc='/api/docs/'
        )

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
api.add_namespace(ns4)
api.add_namespace(ns5)
api.add_namespace(temp_ns6)
