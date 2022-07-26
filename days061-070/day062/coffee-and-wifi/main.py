from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

from backend.forms import AddCafeForm
from backend.data import CafeDatabase

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

database = CafeDatabase()

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cafes')
def cafes():
    return render_template('cafes.html', cafes=database.load())


@app.route('/cafes/add', methods=['GET', 'POST'])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        legacy_db = database.load()
        new_row = [form.cafe_name.data, form.location_url.data, form.open_time.data, form.close_time.data,
                   form.coffee_rating.data, form.wifi_rating.data, form.power_availability_rating.data]
        legacy_db.append(new_row)
        database.update(legacy_db)
        return render_template('cafes.html', cafes=legacy_db)

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
