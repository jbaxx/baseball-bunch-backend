from flask_restplus import Namespace, Resource

api = Namespace('players', description= 'The players')

@api.route('')
class Players(Resource):
    def get(self):
        """
        All players
        """
        return {'player': 'larry walker'}
