import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api

# Implemented
from .users                   import api as ns1
from .token                   import api as ns2
from .player                  import api as ns3
from .players                 import api as ns4
from .fantasy_team            import api as ns5
from .fantasy_team_lineup     import api as ns6
from .search                  import api as ns7
from .sentry_debug            import api as sentry_debug

# In progress
# from .batting          import api as ns15
# from .pitching         import api as ns16
# from .teams            import api as ns17
# from .teams_franchises import api as ns18

from .api_content import api as temp_ns6

authorizations = {
        'Bearer Auth': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            },
        'Basic Auth': {
            'type': 'basic',
            'in': 'header',
            'name': 'authorization',
            }
        }

api = Api(
        title='The Baseball Bunch - Fantasy Baseball Analysis Toolkit',
        version='1.0',
        description='Predict and improve your fantasy game',
        # security='Bearer Auth',
        authorizations=authorizations,
        doc='/api/docs/'
        )

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
api.add_namespace(ns4)
api.add_namespace(ns5)
api.add_namespace(ns6)
api.add_namespace(ns7)
api.add_namespace(sentry_debug)

api.add_namespace(temp_ns6)
