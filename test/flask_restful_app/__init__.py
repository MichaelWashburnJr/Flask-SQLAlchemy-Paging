"""
This is a Flask RESTful application used
for testing the flask_sqlalchemy_paging package.
"""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .database import configure_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
configure_db(app)

api = Api(app)

from . import resources
api.add_resource(resources.PeopleWithFunction, '/people1')
api.add_resource(resources.PeopleWithDecorator, '/people2')


if __name__ == '__main__':
    app.run(debug=True)
