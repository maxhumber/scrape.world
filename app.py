import os
from pathlib import Path
import random

from flask import Flask, jsonify, render_template
from flask_simplelogin import SimpleLogin, login_required
import pandas as pd

import config

app = Flask(__name__)
app.config["SECRET_KEY"] = config.secret
SimpleLogin(app, login_checker=config.login_checker)

# home


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/challenges")
def challenges():
    pages = ["soup", "titans", "sports", "fish", "books"]
    return render_template("challenges.html", pages=pages)


# basics


@app.route("/soup")
def soup():
    return render_template("soup.html")


@app.route("/titans")
def titans():
    return render_template("titans.html")


# sports


@app.route("/sports")
def sports():
    pages = ["spend", "season", "results"]
    return render_template("sports.html", pages=pages)


@app.route("/spend")
def spend():
    return render_template("spend.html")


@app.route("/results")
@login_required()
def results():
    return render_template("results.html")


@app.route("/season")
@login_required()
def season():
    return render_template("season.html")


@app.route("/results_data")
def results_data():
    df = pd.read_csv("data/games.csv")
    data = {"data": df.to_dict(orient="records")}
    return jsonify(data)


# books


@app.route("/books")
def books():
    sale = [0.8, 0.2]
    price = {
        "early": random.choices([28, 0], weights=sale)[0],
        "filthy": random.choices([15, 0], weights=sale)[0],
        "orconomics": random.choices([20, 0], weights=sale)[0],
    }
    return render_template("books.html", price=price)


@app.route("/fish")
def fish():
    return render_template("fish.html")


@app.route("/loaderio-217048ac16b29b838078bfdd254c773c")
def loaderio():
    return 'loaderio-217048ac16b29b838078bfdd254c773c'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
