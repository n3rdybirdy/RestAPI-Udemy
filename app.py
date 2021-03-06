from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Item, Itemlist
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # save resources, SQLAl has its own mod tracker
app.secret_key = "susi"
# Create an API that allows us to add resources to the app
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()                                     # based on config above, could also be different type of db!

jwt = JWT(app, authenticate, identity)                  # /auth

api.add_resource(Item, '/item/<string:name>')           # http://127.0.0.1:5000/item/book
api.add_resource(Itemlist, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)