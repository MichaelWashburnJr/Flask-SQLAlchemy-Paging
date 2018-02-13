"""
Defines the temp database connection for the app.
"""
from flask_sqlalchemy import SQLAlchemy

db = None

def configure_db(app):
    """
    Configure the db value by connecting to a database using the app config.
    """
    global db
    db = SQLAlchemy(app)