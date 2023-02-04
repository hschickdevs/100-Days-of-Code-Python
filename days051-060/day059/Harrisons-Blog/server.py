from backend.forms import CreatePostForm, RegistrationForm, LoginForm
from backend.util import send_contact_email
from backend.config import ADMINISTRATOR_USERNAME
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.datastructures import MultiDict
from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import datetime as dt
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()  # Setup environment variables before server starts


# APP SETUP
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# USER SESSION SETUP
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# DATABASE SETUP
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backend/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    username = db.Column(db.String(250), unique=True,
                         nullable=False, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), unique=True, nullable=False)
    posts = db.relationship('BlogPost', backref='user', lazy=True)

    def get_id(self):
        return self.username


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), db.ForeignKey('user.username'), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

def load_posts(id: int = None):
    if id is None:
        return BlogPost.query.order_by(BlogPost.id.desc()).all()
    else:
        return BlogPost.query.filter_by(id=id).first()


def create_id():
    try:
        return BlogPost.query.order_by(BlogPost.id.desc()).first().id + 1
    except AttributeError:
        # If there are no posts in the database, return 1
        return 1

# ADMINSTRATOR ONLY DECORATOR:


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.username != ADMINISTRATOR_USERNAME:
            flash('Only the site administrator is authorized to access this page.')
            return redirect(url_for('error'))
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def load_user(username):
    # since the username is just the primary key of our user table, use it in the query for the user
    return User.query.get(str(username))

# db.create_all()

# APP ROUTES
@app.route('/')
def home():
    by_user = request.args.get('username')
    return render_template("index.html", posts=load_posts(), username=by_user)


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
@login_required
@admin_only
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
@login_required
@admin_only
def delete_post(p_id: int):
    post = load_posts(p_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/new-post', methods=["GET", "POST"])
@login_required
@admin_only
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
                        author=current_user.username,
                        img_url=form.img_url.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('new-post.html', form=form, editing=False)


# Create a new route to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # Check if user already exists:
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists! Please try a different one.')
            return redirect(url_for('register'))

        # Add new user to the database
        user = User(username=form.username.data,
                     email=form.email.data,
                     password=generate_password_hash(form.password.data, method='sha256'))
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

# Create a new route to handle logins


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST' and form.validate():
        # Check if user exists
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # Check if password is correct
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Invalid password. Please try again.')
                return redirect(url_for('login'))
        else:
            flash('Username does not exist. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


# logout authenticated user
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# route for error


@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)
