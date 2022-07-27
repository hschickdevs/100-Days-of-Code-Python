from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, URL

class AddBookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])

    author = StringField("Author", validators=[DataRequired()])

    rating = IntegerField("Rating (1 - 10)", validators=[DataRequired()])
    
    icon = StringField("Book Icon URL")

    submit = SubmitField('Submit')
    
class EditBookForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired()])

    author = StringField("Author", validators=[DataRequired()])

    rating = IntegerField("Rating (1 - 10)", validators=[DataRequired()])
    
    icon = StringField("Book Icon URL")

    submit = SubmitField('Submit')
    
