from flask import Flask
from flask import json
from flask import Response
import logging
app = Flask(__name__)

FORMAT = '%(asctime)s %(message)s endpoint was reached'
logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename='app.log')

@app.route("/")
def hello():
    logging.debug("/")
    return "Hello World!"

@app.route("/metrics")
def metrics():
    logging.debug("/metrics")
    return Response(
        response=json.dumps({ "data": { "UserCount": 140, "UserCountActive": 23}}),
        status=200,
        content_type="application/json"
    )

@app.route("/status")
def status():
    logging.debug("/status")
    return Response(
        response=json.dumps({ "result": "OK - healthy" }),
        status=200,
        content_type="application/json"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
