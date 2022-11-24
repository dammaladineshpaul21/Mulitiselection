from flask import Flask
from flask_restful import Api
from main import Mulitiselection


def main():
    # creating the flask app
    app = Flask(__name__)
    # creating an API object
    api = Api(app)
    api.add_resource(Mulitiselection, '/square/mulitiselection')
    return app


# driver function
if __name__ == '__main__':
    main().run(debug=True)
