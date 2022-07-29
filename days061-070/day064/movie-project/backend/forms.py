from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired


class EditMovieRatingForm(FlaskForm):
    rating = FloatField('Your Rating (0 - 10, e.g. 7.5)', validators=[DataRequired()])
    
    review = StringField('Your Review', validators=[DataRequired()])
    
    submit = SubmitField('Submit')
    
class AddMovieForm(FlaskForm):
    pass

class SearchMovieForm(FlaskForm):
    title = StringField('Movie Title:', validators=[DataRequired()])
    
    submit = SubmitField('Search')