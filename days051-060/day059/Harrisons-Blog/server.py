from flask import Flask, render_template
import requests


BLOG_URL = "https://api.npoint.io/d9f83de217d4c0cc9a66"

def load_posts():
    return requests.get(BLOG_URL).json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=load_posts())


@app.route('/index.html')
def index():
    return render_template("index.html", posts=load_posts())


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/post.html')
def post():
    return render_template('post.html')

@app.route('/post/<int:p_id>')
def get_post(p_id):
    return render_template('post.html', post=load_posts()[int(p_id) - 1])


if __name__ == "__main__":
    app.run(debug=True)