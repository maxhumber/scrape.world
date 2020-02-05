import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='templates')

df = pd.read_csv('hockey.csv')
df = (df
    [['date', 'team', 'opponent', 'outcome']]
    .drop_duplicates()
    .reset_index(drop=True)
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index_get_data')
def stuff():
    data = {'data': df.to_dict(orient='records')}
  # Assume data comes from somewhere else
    # data = {
    # "data": [
    #   {
    #     "id": "1",
    #     "name": "John Q Public",
    #     "position": "System Architect",
    #     "salary": "$320,800",
    #     "start_date": "2011/04/25",
    #     "office": "Edinburgh",
    #     "extn": "5421"
    #   },
    #   {
    #     "id": "2",
    #     "name": "Larry Bird",
    #     "position": "Accountant",
    #     "salary": "$170,750",
    #     "start_date": "2011/07/25",
    #     "office": "Tokyo",
    #     "extn": "8422"
    #   }]
    # }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
