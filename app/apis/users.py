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
from .. import token_auth


api = Namespace('api/users', description= 'The users')

@auth.verify_password
def verify_password(username, password):
    user = UserModel().get_by_username(username)
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

@token_auth.verify_token
def verify_token(token):
    user = User().verify_auth_token(token)
    if not user:
        return False
    g.user = user
    return True

# User:       defines a User object
# UserSchema: marshmallow schema to perform actual validations (read/write)
# user_model: restplus documentation for User
# UserModel:  defines the methods to query/interact
#               with the user table in the database


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

    def generate_auth_token(self, expiration = 3600):
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

        self.INSERT_USER_QUERY = """
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
        if len(user) == 0:
            return ()
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
        query = self.INSERT_USER_QUERY

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
