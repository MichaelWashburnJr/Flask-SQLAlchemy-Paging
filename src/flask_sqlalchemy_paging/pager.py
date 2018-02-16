"""
Defines functions to page SQLAlchemy queries and return them.
"""
import math
from flask_restful import reqparse, abort, marshal
from flask_sqlalchemy_paging import SETTINGS

def get_params(page_size, page):
    """
    Parses query param arguments and returns the parameters
    needed for paging.

    :returns: a tuple consisting of page_size and page.
    """
    parser = reqparse.RequestParser()

    if SETTINGS.get('ALLOW_PAGE_SIZE_QUERY_PARAM') is True:
        parser.add_argument(
            'page_size',
            type=int,
            default=SETTINGS.get('DEFAULT_PAGE_SIZE'),
            help='page_size is the number of entries to show per page.')

    parser.add_argument(
        'page',
        type=int,
        default=0,
        help='page is the index of the section of entries to show.')

    args = parser.parse_args()

    if page is False:
        page = args.get('page')

    page_size_val = None
    if page_size is False:
        if SETTINGS.get('ALLOW_PAGE_SIZE_QUERY_PARAM') is True:
            page_size_val = args.get('page_size')
        else:
            page_size_val = SETTINGS.get('DEFAULT_PAGE_SIZE')

    return page_size_val, page



def page_query(query, formatter=None, marshal_fields=None, page_size=False, page=False):
    """
    Gets the page and page size (if applicable) from the request and pages the query
    accordingly
    """
    if formatter is None and marshal_fields is None:
        raise ValueError("formatter or marshal_fields must be given a value.")

    num_pages = 1
    total_results = query.count()

    page_size, page = get_params(page_size, page)

    if page_size is not None:
        num_pages = math.ceil(total_results / page_size)

        if page >= num_pages:
            return abort(400, 'The requested page ({0}) is out of range. The maximum page')

        offset = page * page_size
        query = query.offset(offset).limit(page_size)

    num_returned = query.count()
    results = query.all()

    if formatter is not None:
        results = formatter(results)
    elif marshal_fields is not None:
        results = marshal(results, marshal_fields)

    return {
        'page': page,
        'total_pages': num_pages,
        'total_results': total_results,
        'num_returned': num_returned,
        'results': results
    }
