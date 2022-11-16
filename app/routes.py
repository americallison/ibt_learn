
from app import app, db, bcrypt
from flask import Flask, request, render_template, flash, get_flashed_messages,\
    redirect, url_for
from flask_login import current_user
from forms import LoginForm, RegisterForm
from models import User


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(full_name=form.full_name.data,
                    email=form.email.data,
                    user_name=form.user_name.data,
                    contact=form.contact.data,
                    program=form.program.data,
                    address=form.addres.data,
                    password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful', 'info')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title="Register Student")


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/announcements')
def announcements():
    return render_template('announcements.html')


@app.route('/videos')
def videos():
    return render_template('videos.html')


@ app.route('/teaching_model')
def teaching_model():
    return render_template('teaching_model.html')


@app.route('/staff')
def staff():
    return render_template('staff.html')


@app.route('/labs')
def labs():
    return render_template('labs.html')


@app.route('/donate')
def donate():
    return render_template('donate.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')