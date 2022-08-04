from dotenv import load_dotenv
load_dotenv()  # Setup environment variables before server starts

import os
from datetime import datetime as dt
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor, CKEditorField
from werkzeug.datastructures import MultiDict

from backend.util import send_contact_email
from backend.forms import CreatePostForm

### APP SETUP
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

### DATABASE SETUP
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backend/posts.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    
def load_posts(id: int = None):
    if id is None:
        return BlogPost.query.order_by(BlogPost.id.desc()).all()
    else:
        return BlogPost.query.filter_by(id=id).first()

def create_id():
    return BlogPost.query.order_by(BlogPost.id.desc()).first().id + 1
    
    
### APP ROUTES
@app.route('/')
def home():
    return render_template("index.html", posts=load_posts())


@app.route('/index')
def index():
    return render_template("index.html", posts=load_posts())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        subject = f"Contact Form Submission from {request.form['name']}"
        message = f"Name: {request.form['name']}\n" \
                  f"Email: {request.form['email']}\n" \
                  f"Phone #: {request.form['phone']}\n" \
                  f"\nMessage:\n{request.form['message']}"
        send_contact_email(subject, message)
        return render_template('contact.html', form_submitted=True)
    else:    
        return render_template('contact.html', form_submitted=False)


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/post/<int:p_id>')
def get_post(p_id: int):
    return render_template('post.html', post=load_posts(p_id))


@app.route('/edit-post/<int:p_id>', methods=["GET", "POST"])
def edit_post(p_id: int):
    post = load_posts(p_id)
    form = CreatePostForm(data=MultiDict(post.__dict__))
    
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        db.session.commit()
        
        return redirect(url_for('home'))
    
    return render_template('new-post.html', form=form, editing=True, post_id=p_id)


@app.route('/delete-post/<int:p_id>', methods=["GET"])
def delete_post(p_id: int):
    post = load_posts(p_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        if os.name != "nt":
            date_now = dt.now().strftime("%B %d, %Y at %-I:%M%p %Z")
        else:
            date_now = dt.now().strftime("%B %d, %Y at %I:%M%p %Z")
        post = BlogPost(id=create_id(),
                        title=form.title.data, 
                        subtitle=form.subtitle.data, 
                        date=date_now, 
                        body=form.body.data, 
                        author=form.author.data, 
                        img_url=form.img_url.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('new-post.html', form=form, editing=False)


if __name__ == "__main__":
    app.run(debug=True)