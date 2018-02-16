import unittest
import requests
import json
import sys
from test import flask_restful_app
from test.flask_restful_app.database import db
from test.flask_restful_app import models


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = flask_restful_app.app.test_client()
        db.create_all()
        # seed some people into the database
        names = [
            'John',
            'Jim',
            'Mike',
            'Frodo',
            'Harry'
        ]
        for name in names:
            person = models.Person.query.filter_by(name=name).first()
            if person is None:
                person = models.Person(name=name)
                db.session.add(person)
        db.session.commit()

    def test_people_with_function(self):
        response = self.app.get('/people1')
        self.assertEqual(response.status_code, 200)
        results = json.loads(response.get_data())
        self.assertTrue(len(results) > 0)

    def test_people_with_decorator(self):
        response = self.app.get('/people2')
        self.assertEqual(response.status_code, 200)
        results = json.loads(response.get_data())
        self.assertTrue(len(results) > 0)