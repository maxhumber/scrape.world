secret = 'super-secret-secret'

users = {
    'max': {'password': 'gazpacho'},
    'admin': {'password': 'admin'}
}

def login_checker(user):
    user_data = users.get(user['username'])
    if not user_data:
        return False
    elif user_data.get('password') == user['password']:
        return True
    return False
