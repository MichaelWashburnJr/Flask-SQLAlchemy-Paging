"""
This defines the resources used for the test project.
"""
from flask_restful import Resource, fields, marshal_with
import models


person_fields = {
    'id': fields.Integer,
    'name': fields.String
}

class People(Resource):
    """
    A resource class which defines a paged API endpoint
    returing a list of people.
    """
    
    @marshal_with(person_fields)
    def get(self):
        query = models.Person.query
        return query.all()