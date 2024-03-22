from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread
import time

app = Flask(__name__)
CORS(app)


def start_logic():
    print("logic started")


@app.route('/api/data')
def get_data():
    print('YEEES')
    data = {'message': 'Hello from Python backend!'}
    return jsonify(data)


if __name__ == '__main__':
    thread = Thread(target=start_logic)
    thread.start()
    app.run(debug=True)
