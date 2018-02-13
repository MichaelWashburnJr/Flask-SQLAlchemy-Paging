from setuptools import find_packages, setup

setup(
    name='flask_sqlalchemy_paging',
    version='0.0.1',
    description='Painless Paging Flask and SQLAlchemy',
    author='Michael Washburn Jr',
    author_email='michael@michaelwashburnjr.com',
    url='https://github.com/MichaelWashburnJr/Flask-SQLAlchemy-Paging',
    packages=find_packages('src'),
    install_requires=[
    ],
    tests_require=[
        'nose==1.3.7',
        'Flask==0.12.2',
        'Flask-RESTful==0.3.6',
        'Flask-SQLAlchemy==2.3.2',
        'SQLAlchemy==1.2.2',
    ],
)