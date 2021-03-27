from flask import jsonify
from flask import g
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields as rest_fields

from .. import auth


api = Namespace('api/token', description= 'The token')

token_model = api.model('Token', {
    'token': rest_fields.String,
    })

@api.route('')
class Token(Resource):
    @api.doc(security='Basic Auth')
    @api.response(200, 'Success', token_model)  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @auth.login_required
    def get(self):
        """
        Retrieves a token for a user
        """
        token = g.user.generate_auth_token()
        return jsonify({ 'token': token.decode('ascii') })
