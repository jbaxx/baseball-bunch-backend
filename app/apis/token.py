from flask import jsonify, g
from flask_restplus import Namespace
from flask_restplus import Resource

from .. import auth


api = Namespace('api/token', description= 'The token')

@api.route('')
class Token(Resource):
    @api.doc(security='Basic Auth')
    @auth.login_required
    def get(self):
        """
        Retrieves a token for a user
        """
        token = g.user.generate_auth_token()
        return jsonify({ 'token': token.decode('ascii') })
