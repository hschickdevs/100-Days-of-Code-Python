from dotenv import load_dotenv
from werkzeug.datastructures import MultiDict
import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from backend.forms import EditMovieRatingForm, AddMovieForm, SearchMovieForm
from backend.omdb import OMDBClient

load_dotenv()

# Setup app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backend/movies.sqlite'

# Set frameworks
Bootstrap(app)
db = SQLAlchemy(app)
tmdb = OMDBClient(api_key=None)  # Using environment variable


# Setup database
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(4), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float(8), unique=False, nullable=True)
    review = db.Column(db.String(250), unique=False, nullable=True)
    img_url = db.Column(db.String(250), unique=False, nullable=True)

db.create_all()


@app.route("/")
def home():
    return render_template("index.html", movies=Movie.query.order_by(Movie.rating.desc()).all())

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    form = EditMovieRatingForm(data=MultiDict({"rating": movie.rating, "review": movie.review}))
    
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("edit.html", form=form)


@app.route("/delete/<int:movie_id>", methods=["GET", "POST"])
def delete(movie_id):
    del_movie = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(del_movie)
    
    db.session.commit()
    
    return redirect(url_for("home"))


@app.route("/search", methods=["GET", "POST"])
def search_movies():
    form = SearchMovieForm()
    
    if form.validate_on_submit():
        # Get movie data from TMDB
        movies = tmdb.search_movies(query=form.title.data)
        return render_template("select.html", movies=movies)
    
    return render_template("add.html", form=form)


@app.route("/add/<int:tmdb_movie_id>", methods=["GET", "POST"])
def add_movie(tmdb_movie_id):
    movie_data = tmdb.get_movie(movie_id=tmdb_movie_id)
    db_movie = Movie(id=movie_data.id,
                     title=movie_data.title, 
                     year=movie_data.release_year, 
                     description=movie_data.description, 
                     img_url=movie_data.img_url,
                     rating=None,
                     review=None)
    db.session.add(db_movie)
    db.session.commit()
    
    return redirect(url_for("edit", movie_id=db_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
