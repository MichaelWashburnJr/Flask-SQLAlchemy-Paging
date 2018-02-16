"""
Defines decorators to simplify usage and keep resources
simple.
"""
from .pager import page_query

def paged_query(formatter=None, marshal_fields=None):
    """
    Decorator for paging a query
    
    :param: formatter
    :type formatter: function
    :returns: a dict with values to represent as a json response.
    """
    if formatter is None and marshal_fields is None:
        raise ValueError("formatter or marshal_fields must be given a value.")

    def decorator(method):
        def wrapper(self):
            query = method(self)
            response = page_query(query, formatter=formatter, marshal_fields=marshal_fields)
            return response
        return wrapper
    return decorator
