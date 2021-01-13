from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

users = {
    'users_list':
    [
        {
            'id': 'xyz789',
            'name': 'Charlie',
            'job': 'Janitor',
        },
        {
            'id': 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id': 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'id': 'yat999',
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id': 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}


@app.route('/users/<user_id>', methods=['GET', 'DELETE'])
def get_user(user_id):
    if request.method == 'GET':
        for user in users['users_list']:
            if user_id == user['id']:
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
    search_username = request.args.get('name')
    if request.method == 'GET':
        if search_username:
            subdict = {'users_list': []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        return resp
    raise Exception("Unsupported method")


@app.route('/')
def hello_world():
    return 'Hello, world!'
