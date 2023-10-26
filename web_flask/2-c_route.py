#!/usr/bin/python3
''' Hello Flask! '''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
