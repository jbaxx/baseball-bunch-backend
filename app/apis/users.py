from flask import make_response, jsonify, abort, request, g, current_app
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields as rest_fields
from marshmallow import fields, ValidationError, Schema
from MySQLdb import ProgrammingError
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import MySQLdb.cursors

from .. import db
from .. import auth


api = Namespace('users', description= 'The users')

# @auth.verify_password
# def verify_password(username, password):
#     user = UserModel().get_by_username(username)
#     if not user or not user.verify_password(password):
#         return False
#     g.user = user
#     return True

@auth.verify_password
def verify_password(username_or_token, password):
    user = User().verify_auth_token(username_or_token)
    if not user:
        user = UserModel().get_by_username(username_or_token)
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

# To add new field
# 1. Add it to the Object class
# 2. Add it to the ObjectSchema class
class User:
    def __init__(self, **kwargs):
        self.userid = kwargs.get('userid', '')
        self.username = kwargs.get('username', '')
        self.emailAddress = kwargs.get('emailAddress', '')
        self.password = kwargs.get('password', '')

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in = expiration)
        return s.dumps({'id': self.userid})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # token was valid, but expired
        except BadSignature:
            return None # invalid token
        user = UserModel().get_by_id(data['id'])
        return user


@api.route('/token')
class Token(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        return jsonify({ 'token': token.decode('ascii') })


# Marshmallow Schema
class UserSchema(Schema):
    userid = fields.String()
    username = fields.String(data_key='username', required=True)
    password = fields.String(required=True, load_only=True)
    emailAddress = fields.String(required=True)

# rest_plus schema
user_model = api.model('User', {
    # 'userid': rest_fields.String,
    'username': rest_fields.String,
    'password': rest_fields.String,
    'emailAddress': rest_fields.String,
    })

@api.route('')
class AllUsers(Resource):
    """
    Users
    """
    def get(self):
        """
        Lists all users
        """
        users = UserModel().get_all()
        return make_response(jsonify(users), 200)

    @api.response(201, 'User created')  # Api documentation
    @api.response(422, 'Wrong body schema')  # Api documentation
    @api.expect(user_model, validate=True)
    def post(self):
        """
        Adds a user
        """
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400

        try:
            # Validate the data acquired conforms to the UserSchema (marsh)
            user_data = UserSchema().load(json_data)
        except ValidationError as err:
            return err.messages, 422

        username = user_data.get('username')

        username_exists = UserModel().get_by_username(username)
        if username is None or username == '':
            abort(422)
        if username_exists:
            abort(409, description='User already exists')

        user = User(
                username = user_data.get('username'),
                emailAddress = user_data.get('emailAddress'))
        user.hash_password(user_data.get('password'))

        UserModel().insert_user(user)
        print(UserModel().get_by_username(username))

        return {'message': 'a user created'}, 201


class UserModel:
    def __init__(self):
        self.GET_ALL_QUERY = """
        SELECT
            *
        FROM
            users
        """

        self.GET_BY_ID_QUERY = """
        SELECT
            *
        FROM
            users
        WHERE
            userID = %(user_id)s
        """

        self.GET_BY_USERNAME_QUERY = """
        SELECT
            *
        FROM
            users
        WHERE
            username = %(username)s
        LIMIT 1
        """

        self.INSERT_USER = """
           INSERT INTO users (username, password, emailAddress) VALUES
           (%(username)s, %(password_hash)s, %(email_address)s);
       """

    def get_all(self):
        query = self.GET_ALL_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query)
        except ProgrammingError as err:
            raise err
        users = cursor.fetchall()
        users_list = []
        for u in users:
            print(u)
            users_list.append(User(**u))
        users = UserSchema(many=True).dump(users_list)
        return users

    def get_by_id(self, user_id):
        query = self.GET_BY_ID_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query, {'user_id': user_id})
        except ProgrammingError as err:
            raise err
        user = cursor.fetchall()
        user_result = UserSchema().dump(User(**user[0]))
        return user_result

    def get_by_username(self, username):
        query = self.GET_BY_USERNAME_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query, {'username': username})
        except ProgrammingError as err:
            raise err
        user = cursor.fetchone()
        if user is None:
            return ()
        user_result = User(**user)
        return user_result

    def insert_user(self, user: User):
        query = self.INSERT_USER

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query,
                    {
                        'username': user.username,
                        'password_hash': user.password,
                        'email_address': user.emailAddress
                        })
            db.connection.commit()
        except ProgrammingError as err:
            raise err



@api.route('/<user_id>')
@api.doc(params={'user_id': 'A user ID'})
class SingleUser(Resource):
    """
    User based methods
    """
    @api.response(200, 'Success', user_model)  # Api documentation
    @api.response(400, 'User not found')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
    def get(self, user_id):
        """
        Get a user by id
        """
        try:
            user = UserModel().get_by_id(user_id)
        except ProgrammingError:
            abort(500)

        if not user:
            return {'message': 'User could not be found'}, 400

        # From the cursor result:
        # 1. Create a User object
        # 2. Validate it with UserSchema (marshmallow)
        # 3. The result can be filtered with help of the UserSchema model
        user_result = UserSchema().dump(User(**user[0]))
        return user_result

        # return make_response(jsonify(user_result), 200)


    @api.response(201, 'User created')  # Api documentation
    @api.response(422, 'Wrong body schema')  # Api documentation
    @api.expect(user_model, validate=True)
    def post(self, user_id):
        """
        Adds a user
        """
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400

        try:
            # Validate the data acquired conforms to the UserSchema (marsh)
            data = UserSchema().load(json_data)
        except ValidationError as err:
            return err.messages, 422

        _ = user_id
        _ = data
        # TODO: add user

        return {'message': 'a user created'}, 201
