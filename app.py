import predict
import train as t

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    predict.predict_and_submit()
    return jsonify({"status": "ok"})


@app.route('/train', methods=['GET', 'POST'])
def train():
    t.train()
    return jsonify({"status": "ok"})
