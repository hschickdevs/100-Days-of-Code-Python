from flask import Flask, render_template, request
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[Email("Invalid email format."), DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "secret-key"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("legacy/index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if request.method == "POST":
        # if login_form.validate_on_submit():
        #     print("Form validated!")
        #     print(login_form.email.data)
        #     return render_template("legacy/success.html", form=login_form)
        # else:
        return render_template("bootstrap_support/denied_bootstrap.html")

    else:
        return render_template('bootstrap_support/login_bootstrap_quickform.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)