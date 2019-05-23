import predict
import train as t

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/submit')
def submit():
    predict.predict_and_submit()
    return jsonify({"status": "ok"})


@app.route('/train')
def train():
    t.train()
    return jsonify({"status": "ok"})
