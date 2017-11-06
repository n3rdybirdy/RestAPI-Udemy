import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank")

    def post(self):
        # Need to parse the arguments first before we can work with them
        # get data from JSON payload:
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User not created - already exists"}, 400

        user = UserModel(data['username'], data['password'])        # or (**data) instead
        user.save_to_db()

        return {"message": "User created successfully."}, 201

