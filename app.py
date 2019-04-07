import os

import json
import utils
from flask import Flask, Response, abort

app = Flask(__name__)

@app.route('/files')
def item_list():

    # Create this
    response = Response(
        json.dumps('fixme'), status=200, mimetype='application/json')
    return response


@app.route('/files/<int:pk>')
def item_score(pk):

    # Create this
    score = utils.get_score(pk)

    if score is None:
        abort(404)

    content = json.dumps(score)
    return content, 200, {'Content-Type': 'application/json'}


@app.errorhandler(404)
def not_found(e):
    return '', 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')