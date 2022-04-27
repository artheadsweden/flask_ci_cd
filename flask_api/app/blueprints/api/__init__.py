"""
API Blueprint
"""

import json
from flask import Blueprint, Response


bp_api = Blueprint('bp_api', __name__)

users = [
    {
        'first_name': 'Alice',
        'last_name': 'Anderson',
        'email': 'alice@email.com',
        'city': 'Athens',
        'country': 'Greece'
    },
    {
        'first_name': 'Bob',
        'last_name': 'Benson',
        'email': 'bob@email.com',
        'city': 'Bologna',
        'country': 'Italy'
    },
    {
        'first_name': 'Carl',
        'last_name': 'Cedrick',
        'email': 'carl@email.com',
        'city': 'Cairo',
        'country': 'Egypt'
    },
]


@bp_api.get('/users')
def users_get():
    """
    Getter for users
    returns: Json response
    """
    return Response(json.dumps(users), 200, content_type='application/json')
