from flask_restplus import Api

from .batting import api as ns1
from .pitching import api as ns2
from .players import api as ns3
from .teams import api as ns4
from .teams_franchises import api as ns5
from .users import api as ns6

from .api_content import api as temp_ns6

# authorizations = {
#         'apiKey': {
#             'type': 'apiKey',
#             'in': 'header',
#             'name': 'X-API-KEY',
#             }
#         }

authorizations = {
        'Bearer Auth': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            }
        }

# authorizations = {
#         'Basic Auth': {
#             'type': 'basic',
#             'in': 'header',
#             'name': 'authorization',
#             }
#         }

api = Api(
        title='The Baseball Bunch - Fantasy Baseball Analysis Toolkit',
        version='1.0',
        description='Predict and improve your fantasy game',
        security='Bearer Auth',
        authorizations=authorizations,
        doc='/api/docs/'
        )

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
api.add_namespace(ns4)
api.add_namespace(ns5)
api.add_namespace(ns6)
api.add_namespace(temp_ns6)
