# NOTE: Jinja comes bundled with flask, so there is no need to install it.
from datetime import datetime
import requests
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    random_num = random.randint(1, 10)
    return render_template('index.html', num=random_num, year=datetime.datetime.now().year)


@app.route("/guess/<name>")
def guessify(name):
    year = datetime.now().year
    gender_response = requests.get(f'https://api.genderize.io?name={name}').json()
    gender = gender_response["gender"]
    prob = gender_response['probability']
    ageify_response = requests.get(f'https://api.agify.io/?name={name}').json()
    age = ageify_response['age']
    return render_template('ify.html', name=name, gender=gender, prob=prob, age=age, year=year)

@app.route("/blog")
def blog():
    blog_url = "NO"
    return


if __name__ == "__main__":
    app.run(debug=True)
