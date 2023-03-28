from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, DateTimeField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length


class UserSignUpForm(FlaskForm):
    """For user signup."""

    username = StringField('Username', validators=[
                           DataRequired(), Length(max=30)])
    first_name = StringField('First name', validators=[
                             DataRequired(), Length(max=30)])
    last_name = StringField('Last name', validators=[
                            DataRequired(), Length(max=30)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=5)])


class UserLoginForm(FlaskForm):
    """For user login."""

    username = StringField('Username', validators=[
                           DataRequired(message="Username required.")])
    password = PasswordField('Password', validators=[
                             DataRequired(message="Username required.")])


class UserUpdateForm(FlaskForm):
    """For update user information"""

    username = StringField('Username', validators=[
                           DataRequired(), Length(max=30)])
    first_name = StringField('First name', validators=[
                             DataRequired(), Length(max=30)])
    last_name = StringField('Last name', validators=[
                            DataRequired(), Length(max=30)])
    profile_img = StringField('Profile Image')
    bio = StringField('Bio')
    location = StringField('Location')
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=5)])


class AdventureForm(FlaskForm):
    """For creating a new adventure."""

    title = StringField("Title", validators=[
        DataRequired(), Length(max=100)])
    location = StringField("General Location", validators=[DataRequired()])
    activity = StringField("Activity Type", validators=[
                           DataRequired(), Length(max=30)])
    departure_datetime = DateTimeField(
        "Expected Departure Time",  format='%m-%d-%Y %H:%M', validators=[DataRequired()])

    return_datetime = DateTimeField(
        "Exprected Return Time", format='%m-%d-%Y %H:%M', validators=[DataRequired()])

    notes = TextAreaField("Notes")
    header_img_url = StringField("Image URL")

class WaypointForm(FlaskForm):
    """Form for creating and updating waypoints."""

    lat = DecimalField("Latitude", validators=[
                       DataRequired()], places=8, rounding=None)
    long = DecimalField("Longitude", validators=[
                        DataRequired()], places=8, rounding=None)
    color = SelectField("Waypoint Color", choices=[
                        "red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "brown"])
