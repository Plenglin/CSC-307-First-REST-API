import json

import pytest

from app import app
from model_mongodb import User
from populate import populate_db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def populated_db():
    User.flush()
    populate_db()


@pytest.fixture
def random_user(client):
    resp = client.get('/users')
    data = decode_resp(resp)
    yield data[0]


def decode_resp(resp):
    return json.loads(str(resp.data, encoding='utf8'))


def test_get_users(client, populated_db):
    resp = client.get('/users')

    data = decode_resp(resp)
    assert isinstance(data, list)
    assert len(data) == 6


def test_get_single_user(client, populated_db, random_user):
    uid = random_user['_id']

    resp = client.get(f'/users/{uid}')

    data = decode_resp(resp)
    assert isinstance(data, dict)
    assert data['_id'] == uid


def test_delete_user(client, populated_db, random_user):
    uid = random_user['_id']

    client.delete(f'/users/{uid}')

    resp = client.get('/users')
    data = decode_resp(resp)
    assert isinstance(data, list)
    assert len(data) == 5


def test_create_user(client, populated_db):
    resp = client.post(f'/users', {'name': "Test User", 'job': "Benchwarming"})

    uid = decode_resp(resp)['_id']
    data = decode_resp(client.get(f'/users/{uid}'))
    assert data['_id'] == uid

