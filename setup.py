from setuptools import find_packages, setup

setup(
    name='flask_sqlalchemy_paging',
    version='0.0.1',
    description='Painless Paging Flask and SQLAlchemy',
    author='Michael Washburn Jr',
    author_email='michael@michaelwashburnjr.com',
    url='https://github.com/MichaelWashburnJr/Flask-SQLAlchemy-Paging',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[
        'Flask==0.12.2',
        'Flask-RESTful==0.3.6',
        'Flask-SQLAlchemy==2.3.2',
        'SQLAlchemy==1.2.2',
        'requests==2.18.4',
    ],
    extras_require={
        'test': [
            'nose==1.3.7',
        ]
    }
)