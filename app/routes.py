

from flask import Flask, request, render_template, flash, get_flashed_messages
from app import app, db
from models import User


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/announcements')
def announcements():
    return render_template('announcements.html')


@app.route('/videos')
def videos():
    return render_template('videos.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')