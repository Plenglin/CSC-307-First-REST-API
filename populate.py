from model_mongodb import User

users = {
    'users_list':
    [
        {
            'name': 'Charlie',
            'job': 'Janitor',
        },
        {
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'name': 'Dee',
            'job': 'Actress',
        },
        {
            'name': 'Doo',
            'job': 'Actress',
        },
        {
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}

if __name__ == '__main__':
    for u in users['users_list']:
        x = User(u)
        x.save()
