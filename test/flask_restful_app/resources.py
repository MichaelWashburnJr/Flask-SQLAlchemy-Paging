"""
This defines the resources used for the test project.
"""
from flask_restful import Resource, fields, marshal_with, marshal
from flask_sqlalchemy_paging.pager import page_query
from flask_sqlalchemy_paging.decorators import paged_query
from . import models


person_fields = {
    'id': fields.Integer,
    'name': fields.String
}

class PeopleWithFunction(Resource):
    """
    A resource class which defines a paged API endpoint
    returing a list of people.
    """
    
    def get(self):
        query = models.Person.query
        return page_query(query, marshal_fields=person_fields)

class PeopleWithDecorator(Resource):
    """
    A resource class which defines a paged API endpoint
    returing a list of people.
    """
    
    @paged_query(marshal_fields=person_fields)
    def get(self):
        return models.Person.query
