import json

import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_users(client):
    rv = client.get('/users')
    data = json.loads(str(rv.data, encoding='utf8'))
    assert isinstance(data, list)
    assert len(data) == 6
