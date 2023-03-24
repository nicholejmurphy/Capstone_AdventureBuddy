from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
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
                           DataRequired(), Length(max=30)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=5)])


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
