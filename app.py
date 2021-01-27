from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import random
import string

from model_mongodb import User


def random_string():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))


app = Flask(__name__)
CORS(app)


@app.route('/users/<user_id>', methods=['GET', 'DELETE'])
def get_user(user_id):
    if request.method == 'GET':
        for user in User.find_all(_id=user_id):
            return user
        return jsonify(success=False, status=404)
    elif request.method == 'DELETE':
        to_delete = None
        for i, user in enumerate(users['users_list']):
            if user_id == user['id']:
                del users['users_list'][i]
                return jsonify(success=True)

        return make_response(jsonify(success=False), 404)


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return jsonify(list(User.find_all(**request.args)))
    elif request.method == 'POST':
        userToAdd = {**request.get_json(), 'id': random_string()}
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        return make_response(jsonify(userToAdd), 201)
    raise Exception("Unsupported method")


@app.route('/')
def hello_world():
    return 'Hello, world!'
