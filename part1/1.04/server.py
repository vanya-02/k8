import flask

app = flask.Flask(__name__)


@app.post('/api')
def api():

    return flask.jsonify({"status": "success"})
