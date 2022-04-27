"""
Unittest for users route
"""

import json
from .fixture import client



def test_users_status_code(client):
    """
    Test the api HTTP status code
    :param client: An app test client from the fixture
    :return: None
    """
    response = client.get('/api/v1.0/users')
    assert response.status_code == 200


def test_users_data(client):
    """
    Test the data from a call to the users end-point
    :param client: An app test client from the fixture
    :return: None
    """
    response = client.get('/api/v1.0/users')
    data = json.loads(response.text)
    assert data[0]['first_name'] == 'Alice'
