# DEPLOY PREMADE WEB TEMPLATE WITH FLASK

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

# IMPORTANT INFO:
# 1. When using .html pages in flask, the .html pages must be stored in a templates folder for flask to recognize them.
# 2. When using image assets, css files, and other assets, (static assets) must be stored in a static folder.
