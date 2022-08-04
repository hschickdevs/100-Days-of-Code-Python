from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Poster Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Post Body", validators=[DataRequired()])
    submit = SubmitField("Publish Post")