from flask import Flask, jsonify, render_template
from flask_simplelogin import SimpleLogin, login_required
import pandas as pd

USERS = {
    'max': {'password': 'gazpacho'},
    'admin': {'password': 'admin'}
}

def check_my_users(user):
    user_data = USERS.get(user['username'])
    if not user_data:
        return False
    elif user_data.get('password') == user['password']:
        return True
    return False

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-secret'
SimpleLogin(app, login_checker=check_my_users)

@app.route('/')
def index():
    return render_template('index.html')

# basics

@app.route('/soup')
def soup():
    return render_template('soup.html')

@app.route('/titans')
def titans():
    return render_template('titans.html')

# sports: pesky pages

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

@app.route('/results')
def dt():
    return render_template('results.html')

@app.route('/results_data')
def stuff():
    df = pd.read_csv('data/hockey.csv')
    data = {'data': df.to_dict(orient='records')}
    return jsonify(data)

@app.route('/fish')
def fish():
    return render_template('fish.html')



@app.route('/click')
def click():
    return render_template('click.html')

@app.route('/scroll')
def scroll():
    return render_template('scroll.html')

@app.route('/scroll2')
def scroll2():
    return render_template('scroll2.html')

@app.route('/scroll3')
def scroll3():
    return render_template('scroll3.html')

if __name__ == '__main__':
    app.run(port=5000, use_reloader=True, debug=True)
