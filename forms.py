from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, \
    PasswordField, BooleanField, TextAreaField, DateField, \
    DateTimeField, TimeField
from wtforms.validators import DataRequired, Length, Optional, \
    EqualTo, Email, ValidationError, URL
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


class UploadNoteForm(FlaskForm):
    note_name = StringField('Title', validators=[DataRequired(),
                                                 Length(min=1, max=100)])
    note_description = TextAreaField('Description', validators=[DataRequired(),
                                                              Length(min=1, max=200)])
    note_content_ = FileField('Upload Note',
                              validators=[FileRequired(),
                                          FileAllowed(
                                              ['doc', 'docx', 'pdf', 'jpg', 'pptx', 'ppt'])])
    note_category = SelectField('Category', validators=[DataRequired()],
                                choices=[('None', 'Select Category'),
                                    ('Computer Literacy', 'Computer Literacy'),
                                         ('Web Design & Design Thinking',
                                          'Web Design & Design Thinking'),
                                         ('Python Programming', 'Python Programming'),
                                         ('Networking Fundamentals', 'Networking Fundamentals')])
    add_note = SubmitField('Upload Note')


class UploadVideoForm(FlaskForm):
    video_name = StringField('Title', validators=[DataRequired(),
                                                  Length(min=1, max=100)])
    video_description = TextAreaField('Description', validators=[DataRequired(),
                                                               Length(min=1, max=200)])
    video_content_ = FileField('Upload Video',
                               validators=[FileRequired(),
                                           FileAllowed(
                                               ['mkv', 'mp4', 'wav', 'mpeg'])])
    video_category = SelectField('Category', validators=[DataRequired()],
                                choices=[('None', 'Select Category'),
                                         ('Computer Literacy', 'Computer Literacy'),
                                         ('Web Design & Design Thinking',
                                          'Web Design & Design Thinking'),
                                         ('Python Programming', 'Python Programming'),
                                         ('Networking Fundamentals', 'Networking Fundamentals')])
    add_video = SubmitField('Upload Video')


class UploadInfoForm(FlaskForm):
    info_title = StringField('Title', validators=[DataRequired(),
                                                  Length(min=1, max=100)])
    info_description = TextAreaField('Description', validators=[DataRequired(),
                                                              Length(min=1, max=200)])
    info_image_ = FileField('Upload Info Image',
                            validators=[FileRequired(),
                                        FileAllowed(
                                            ['jpg', 'jpeg', 'png', 'webp'])])
    add_info = SubmitField('Upload Information')


class UploadEventForm(FlaskForm):
    event_title = StringField('Title', validators=[DataRequired(),
                                                   Length(min=1, max=100)])
    event_description = TextAreaField('Description', validators=[DataRequired(),
                                                               Length(min=1, max=200)])
    event_image = FileField('Upload Event Image',
                            validators=[FileRequired(),
                                        FileAllowed(
                                            ['jpg', 'jpeg', 'png', 'webp'])])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    from_time = TimeField('Start time', validators=[DataRequired()])
    to_time = TimeField('End Time', validators=[DataRequired()])
    registration_link = StringField('Registration Link', validators=[DataRequired(),URL()])
    add_event = SubmitField('Upload Event')


