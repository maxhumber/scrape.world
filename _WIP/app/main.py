import random
import string
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    repos = list(string.ascii_letters)
    random_repos = ", ".join(random.choices(repos, k=5))
    return render_template("index.html", random_repos=random_repos)

@app.route("/result", methods=["POST"])
def predict():
    repos = request.form["repos"]
    repos = ",".join([r.strip() for r in repos.split(",")])
    # fake
    suggestions = list(string.ascii_letters)
    random.shuffle(suggestions)
    return render_template("result.html", suggestions=suggestions[:5])

@app.route('/fish')
def fish():
    return render_template('fish.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
