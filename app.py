import random
from pathlib import Path

from flask import Flask, jsonify, render_template
from flask_simplelogin import SimpleLogin, login_required
import pandas as pd

import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.secret
SimpleLogin(app, login_checker=config.login_checker)

# home

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/challenges')
def challenges():
    pages = [
        'soup',
        'titans',
        'spend',
        'season',
        'results',
        'fish',
        'books'
    ]
    return render_template('challenges.html', pages=pages)

# basics

@app.route('/soup')
def soup():
    return render_template('soup.html')

@app.route('/titans')
def titans():
    return render_template('titans.html')

# pesky pages: sports

@app.route('/spend')
@login_required() # protected
def spend():
    return render_template('spend.html')

@app.route('/season')
@login_required() # protected
def season():
    return render_template('season.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/results_data')
def results_data():
    df = pd.read_csv('data/games.csv')
    data = {'data': df.to_dict(orient='records')}
    return jsonify(data)

# schedule: books
# click: books

@app.route('/books')
def books():
    sale = [0.8, 0.2]
    price = {
        'early': random.choices([28, 0], weights=sale)[0],
        'filthy': random.choices([15, 0], weights=sale)[0],
        'orconomics': random.choices([20, 0], weights=sale)[0]
    }
    return render_template('books.html', price=price)

@app.route('/fish')
def fish():
    return render_template('fish.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
