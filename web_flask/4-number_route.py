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
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is_cool'):
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)