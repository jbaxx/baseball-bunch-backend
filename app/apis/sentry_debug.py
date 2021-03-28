from flask_restplus import Namespace, Resource

api = Namespace('api/sentry-debug', description= 'Sentry Debug')

@api.route('')
class DebugSentry(Resource):
    def get(self):
        """
        Debugs Sentry
        """
        lista = []
        a = lista[14]
        division_by_zero = 1 / 0
