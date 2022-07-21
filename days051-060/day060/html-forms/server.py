from flask import Flask, render_template, request

import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    """To access form data (Data transmitted in a POST or PUT request) ues the request.form attribute"""
    print("Data", request.data)
    print("Args:", request.args)
    print("Values:", request.values)
    return f'<h1>Name: {request.form["name"]} | Password: {request.form["password"]}</h1>'


if __name__ == "__main__":
    app.run(debug=True)