from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

NULL = "✘"
COFFEE_RATINGS = ["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
WIFI_RATINGS = [NULL, "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
POWER_RATING = [NULL, "🔋", "🔋🔋", "🔋🔋🔋", "🔋🔋🔋🔋", "🔋🔋🔋🔋🔋"]


class AddCafeForm(FlaskForm):
    cafe_name = StringField('Cafe Name', validators=[DataRequired()])
    location_url = StringField("Cafe Location (Google Maps URL)", validators=[URL(), DataRequired()])
    open_time = StringField("Opening Time (e.g. 8AM)", validators=[DataRequired()])
    close_time = StringField("Closing Time (e.g. 9PM)", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", validators=[DataRequired()], default=COFFEE_RATINGS[0],
                                choices=COFFEE_RATINGS)
    wifi_rating = SelectField("Wifi Strength", validators=[DataRequired()], default=WIFI_RATINGS[0],
                              choices=WIFI_RATINGS)
    power_availability_rating = SelectField("Power Socket Availability", validators=[DataRequired()],
                                            default=WIFI_RATINGS[0], choices=POWER_RATING)
    submit = SubmitField('Submit')