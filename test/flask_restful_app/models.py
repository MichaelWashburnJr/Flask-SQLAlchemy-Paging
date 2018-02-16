"""
Defines models used by the test app resources.
"""
from sqlalchemy.ext.declarative import declarative_base
from .database import db

class Person(db.Model):
    """
    Defines an object representation of a list of people.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "<Person id='{id}'' name='{name}''>".format(id=self.id, name=self.name)

def create_tables(engine):
    """
    Creates all tables defined with the base class.
    """
    BASE.metadata.create_all(engine)
