from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, URL


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Poster Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Post Body", validators=[DataRequired()])
    submit = SubmitField("Publish Post")


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password')
    accept_tos = BooleanField('I Accept the Terms of Service', [validators.DataRequired()])
    submit = SubmitField("Sign Me Up!")