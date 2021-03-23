from flask import make_response, jsonify, abort, request
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields as rest_fields
from marshmallow import fields, ValidationError, Schema
from MySQLdb import ProgrammingError
from passlib.apps import custom_app_context as pwd_context
import MySQLdb.cursors

from .. import db


api = Namespace('users', description= 'The users')

# To add new field
# 1. Add it to the Object class
# 2. Add it to the ObjectSchema class
class User:
    def __init__(self, **kwargs):
        self.userid = kwargs.get('userid', '')
        self.username = kwargs.get('username', '')
        self.emailAddress = kwargs.get('emailAddress', '')
        self.password_hash = ''

    def hash_password(self, password):
        self.passord_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


# Marshmallow Schema
class UserSchema(Schema):
    userid = fields.String()
    username = fields.String(data_key='username', required=True)
    password = fields.String(required=True)
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

        print(user_data)
        username = user_data.get('username')

        username_exists = UserModel().get_by_username(username)
        if username is None or username == '':
            abort(422)
        if username_exists:
            abort(409, description="User already exists")

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
        return users

    def get_by_id(self, user_id):
        query = self.GET_BY_ID_QUERY
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query, {'user_id': user_id})
        except ProgrammingError as err:
            raise err
        user = cursor.fetchall()
        return user

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
        user_result = UserSchema().dump(User(**user))
        return user_result

    def insert_user(self, user: User):
        query = self.INSERT_USER

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(query,
                    {
                        'username': user.username,
                        'password_hash': user.password_hash,
                        'email_address': user.emailAddress
                        })
            # cursor.executemany(query,
            #         [(user.username, user.password_hash, user.emailAddress)])
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
