from flask import Flask, jsonify, render_template
from flask.views import MethodView
from flask_simplelogin import SimpleLogin, get_username, login_required

USERS = {
    'max': {'password': 'gazpacho'},
    'admin': {'password': 'admin'}
}

def check_my_users(user):
    user_data = USERS.get(user['username'])
    if not user_data:
        return False  # <--- invalid credentials
    elif user_data.get('password') == user['password']:
        return True  # <--- user is logged in!
    return False  # <--- invalid credentials

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-secret'
SimpleLogin(app, login_checker=check_my_users)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/soup')
def soup():
    return render_template('soup.html')

@app.route('/caps')
def caps():
    return render_template('caps.html')

@app.route('/points')
def points():
    return render_template('points.html')

@app.route('/secret')
@login_required()
def secret():
    return render_template('secret.html')

if __name__ == '__main__':
    app.run(port=5000, use_reloader=True, debug=True)
