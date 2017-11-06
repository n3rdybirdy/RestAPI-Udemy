import sqlite3
from db import db

class UserModel(db.Model):

    # Define the table name under which we want to store out objects
    __tablename__ = "users"

    # create columns for things that get saved to DB, use same names as below in the init
    id = db.Column(db.Integer, primary_key=True)    # create column for ID, prim key to make it unique
    username = db.Column(db.String(80))             # limits size of string to 80 characters
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):

        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
