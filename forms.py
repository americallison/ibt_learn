from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, \
    PasswordField, BooleanField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Optional, \
    EqualTo, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from models import User


# form to register user
class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(),
                                                       Length(min=1, max=50)])
    user_name = StringField('Username', validators=[DataRequired(),
                                                       Length(min=1, max=50)])
    email = StringField('Email', validators=[Optional(),
                                             Length(min=1, max=50)])
    contact = StringField('Contact', validators=[DataRequired(),
                                                 Length(min=10, max=12)])
    program = SelectField('Program', validators=[DataRequired()],
                                                 choices=
                                                 [('None', 'Select Program'),
                                                     ('Computer Literacy', 'Computer Literacy'),
                                                  ('Python and Web Design', 'Python and Web Design'),
                                                  ('Networking', 'Networking')])
    address = StringField('Address', validators=[DataRequired(),
                          Length(min=1, max=200)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8, max=50)])
    password_repeat = PasswordField('Repeat Password', validators=[EqualTo(
        'password', message='Passwords must match')])
    sign_up = SubmitField('Register Student')

    # check whether a username already exists
    def validate_user_name(self, user_name):
        user = User.query.filter_by(user_name=user_name.data).first()
        if user:
            raise ValidationError("Username has been taken. Please enter another.")

    # check whether an email already exists
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email has been taken. Please enter another.")


# form to log in user
class LoginForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=1, max=50)])
    remember_me = BooleanField('Remember me', validators=[Optional()])
    sign_in = SubmitField('Sign in')

