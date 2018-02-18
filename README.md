# Flask-SQLAlchemy-Paging ![status](https://travis-ci.org/MichaelWashburnJr/Flask-SQLAlchemy-Paging.svg?branch=master)

Painless Paged API Endpoints with Flask and SQLAlchemy

## Description

Flask-SQLAlchemy-Paging is a small package which provides a means to split query results into multiple paged requests.


Example without paging:
```
GET /people
[
  {
    id: 0,
    name: 'Luke'
  },
  {
    id: 1,
    name: 'Han'
  }
]
```

Example with paging:
```
GET /people?limit=1&page=0
{
  page: 0,
  total_pages: 2,
  total_results: 2,
  num_returned: 1,
  results: [
    {
      id: 0,
      name: 'Luke'
    }
  ]
}
```
So why would you want to page your API requests?

- If your requests take too much time
- AND if you can't reduce the size of the objects being returned
- AND if gzip compression isn't good enough
- AND if caching isn't good enough

## Usage

### Decorator
The best way to use Flask-SQLAlchemy-Paging is by using the decorator provided.

```
from flask_restful import Resource
from flask_sqlalchemy_paging.decorators import paged_query
from fields import my_fields

class MyResource(Resource):

    @paged_query(marshal_fields=my_fields)
    def get(self):
      return models.MyModel.query
```
