import os

import json
import pandas as pd
from api import utils
from flask import Flask, Response, abort

app = Flask(__name__)

data = pd.read_csv('data/data.csv')

@app.route('/update')
def item_list():

    # Create this
    response = Response(
        json.dumps('fixme'), status=200, mimetype='application/json')
    return response


@app.route('/get/<int:pk>')
def item_score(pk):

    # Create this
    score = utils.get_score(pk)

    if score is None:
        abort(404)

    content = json.dumps(score)
    return content, 200, {'Content-Type': 'application/json'}

@app.route('/')
def sample():
    return 'Welcome to this sample app :)'


@app.errorhandler(404)
def not_found(e):
    return '', 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')