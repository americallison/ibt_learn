from app import app, db
from flask import request, render_template, flash, redirect, url_for, session
from flask_login import current_user, login_user, login_required, logout_user
from forms import LoginForm, RegisterForm, UploadVideoForm, UploadNoteForm, \
    UploadInfoForm, UploadEventForm
from models import User, Video, Notes, Information, Events, Category
from werkzeug.utils import secure_filename
import uuid
import os
from config import Config
from sqlalchemy import desc, asc


@app.route('/')
@app.route('/home')
def index():
    all_news = Information.query.all()
    all_events = Events.query.all()
    return render_template('index.html', all_news=all_news, all_events=all_events)


@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegisterForm()
    if session['username'] == 'Admin':
        if form.validate_on_submit():
            user = User(full_name=form.full_name.data,
                        email=form.email.data,
                        user_name=form.user_name.data,
                        contact=form.contact.data,
                        program=form.program.data,
                        address=form.address.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful', 'info')
    else:
        flash("The page you are trying to access is restricted", "danger")
        return redirect(url_for('index'))
    return render_template('register.html', form=form, title="Register Student")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        session['username'] = form.user_name.data
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page and next_page.startswith('/') \
                else redirect(url_for('index'))
        else:
            flash("Username or password is not correct", "danger")
    return render_template('login.html', form=form, title="Login")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'danger')
    return redirect(url_for('index'))


@app.route('/announcements')
def announcements():
    return render_template('announcements.html')


@app.route('/videos')
def videos():
    video = Video.query.all()
    return render_template('videos.html', video=video)


@app.route('/teaching_model')
def teaching_model():
    return render_template('teaching_model.html')


@app.route('/comp_literacy')
def comp_literacy():
    note_category = Notes.query.join(Category).add_columns \
        (Category.category_name, Notes.note_name, Notes.note_description, Notes.upload_time,
         Notes.note_content).filter_by(category_name='Computer Literacy').order_by \
        (desc(Notes.upload_time)).limit(8)
    video_category = Video.query.join(Category).add_columns \
        (Category.category_name, Video.video_name, Video.video_description, Video.upload_time,
         Video.video_content).filter_by(category_name='Computer Literacy').order_by \
        (desc(Video.upload_time)).limit(8)
    return render_template('comp_literacy.html', note_category=note_category,
                           video_category=video_category, title="Computer Literacy")


@app.route('/comp_literacy_notes')
def comp_literacy_notes():
    page = request.args.get('page', 1, type=int)
    note_category = Notes.query.join(Category).add_columns \
        (Category.category_name, Notes.note_name, Notes.note_description, Notes.upload_time,
         Notes.note_content).filter_by(category_name='Computer Literacy').order_by \
        (desc(Notes.upload_time)).paginate(page=page, per_page=12)
    return render_template('comp_literacy_notes.html', note_category=note_category,
                           title="Computer Literacy Notes")


@app.route('/comp_literacy_videos')
def comp_literacy_videos():
    page = request.args.get('page', 1, type=int)

    video_category = Video.query.join(Category).add_columns \
        (Category.category_name, Video.video_name, Video.video_description, Video.upload_time,
         Video.video_content).filter_by(category_name='Computer Literacy').order_by \
        (desc(Video.upload_time)).paginate(page=page, per_page=12)
    return render_template('comp_literacy_videos.html', video_category=video_category,
                           title="Computer Literacy Videos")


@app.route('/web_design')
def web_design():
    note_category = Notes.query.join(Category).add_columns \
        (Category.category_name, Notes.note_name, Notes.note_description, Notes.upload_time,
         Notes.note_content).filter_by(category_name='Web Design & Design Thinking').order_by \
        (desc(Notes.upload_time)).limit(4)
    video_category = Video.query.join(Category).add_columns \
        (Category.category_name, Video.video_name, Video.video_description, Video.upload_time,
         Video.video_content).filter_by(category_name='Web Design & Design Thinking').order_by \
        (desc(Video.upload_time)).limit(4)
    return render_template('web_design.html', video_category=video_category,
                           note_category=note_category,
                           title="Web Design & Design Thinking")


@app.route('/web_design_notes')
def web_design_notes():
    page = request.args.get('page', 1, type=int)
    note_category = Notes.query.join(Category).add_columns \
        (Category.category_name, Notes.note_name, Notes.note_description, Notes.upload_time,
         Notes.note_content).filter_by(category_name='Web Design & Design Thinking').order_by \
        (desc(Notes.upload_time)).paginate(page=page, per_page=12)
    return render_template('web_design_notes.html', note_category=note_category,
                           title="Web Design & Design Thinking")


@app.route('/web_design_videos')
def web_design_videos():
    page = request.args.get('page', 1, type=int)

    video_category = Video.query.join(Category).add_columns \
        (Category.category_name, Video.video_name, Video.video_description, Video.upload_time,
         Video.video_content).filter_by(category_name='Web Design & Design Thinking').order_by \
        (desc(Video.upload_time)).paginate(page=page, per_page=12)
    return render_template('web_design_videos.html', video_category=video_category,
                           title="Web Design & Design Thinking")


@app.route('/networking')
def networking():
    note_category = Notes.query.join(Category).add_columns \
        (Category.category_name, Notes.note_name, Notes.note_description, Notes.upload_time,
         Notes.note_content).filter_by(category_name='Networking Fundamentals').order_by \
        (desc(Notes.upload_time)).limit(4)
    video_category = Video.query.join(Category).add_columns \
        (Category.category_name, Video.video_name, Video.video_description, Video.upload_time,
         Video.video_content).filter_by(category_name='Computer Literacy').order_by \
        (desc(Video.upload_time)).limit(4)
    return render_template('networking.html', note_category=note_category,
                           video_category=video_category,
                           title="Networking Fundamentals")


@app.route('/networking_notes')
def networking_notes():
    page = request.args.get('page', 1, type=int)
    note_category = Notes.query.join(Category).add_columns \
        (Category.category_name, Notes.note_name, Notes.note_description, Notes.upload_time,
         Notes.note_content).filter_by(category_name='Networking Fundamentals').order_by \
        (desc(Notes.upload_time)).paginate(page=page, per_page=12)
    return render_template('networking_notes.html', note_category=note_category, title="Python Programming")


@app.route('/networking_videos')
def networking_videos():
    page = request.args.get('page', 1, type=int)

    video_category = Video.query.join(Category).add_columns \
        (Category.category_name, Video.video_name, Video.video_description, Video.upload_time,
         Video.video_content).filter_by(category_name='Network Fundamentals').order_by \
        (desc(Video.upload_time)).paginate(page=page, per_page=12)
    return render_template('networking_videos.html', video_category=video_category,
                           title="Networking Fundamentals Videos")


@app.route('/python')
def python():
    note_category = Notes.query.join(Category).add_columns \
        (Category.category_name, Notes.note_name, Notes.note_description, Notes.upload_time,
         Notes.note_content).filter_by(category_name='Python Programming').order_by \
        (desc(Notes.upload_time)).limit(4)
    video_category = Video.query.join(Category).add_columns \
        (Category.category_name, Video.video_name, Video.video_description, Video.upload_time,
         Video.video_content).filter_by(category_name='Python Programming').order_by \
        (desc(Video.upload_time)).limit(4)
    return render_template('python.html', note_category=note_category,
                           video_category=video_category, title="Python Programming")


@app.route('/python_notes')
def python_notes():
    page = request.args.get('page', 1, type=int)
    note_category = Notes.query.join(Category).add_columns \
        (Category.category_name, Notes.note_name, Notes.note_description, Notes.upload_time,
         Notes.note_content).filter_by(category_name='Computer Literacy').order_by \
        (desc(Notes.upload_time)).paginate(page=page, per_page=12)
    return render_template('python_notes.html', note_category=note_category, title="Python Programming Notes")


@app.route('/python_videos')
def python_videos():
    page = request.args.get('page', 1, type=int)

    video_category = Video.query.join(Category).add_columns \
        (Category.category_name, Video.video_name, Video.video_description, Video.upload_time,
         Video.video_content).filter_by(category_name='Python Programming').order_by \
        (desc(Video.upload_time)).paginate(page=page, per_page=12)
    return render_template('python_videos.html', video_category=video_category,
                           title="Python Programming Videos")


@app.route('/staff')
def staff():
    return render_template('staff.html')


@app.route('/labs')
def labs():
    return render_template('labs.html')


@app.route('/donate')
def donate():
    users = User.query.all()
    return render_template('donate.html', users=users)


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/notes_upload', methods=['GET', 'POST'])
@login_required
def notes_upload():
    form = UploadNoteForm()
    if session['username'] == 'Admin':
        if form.validate_on_submit():
            note_to_upload = request.files['note_content_']
            filename = str(uuid.uuid4()) + os.path.splitext(
                secure_filename(note_to_upload.filename))[1]
            note_to_upload.save(os.path.join(Config.UPLOAD_FOLDER_1, filename))
            category = Category(category_name=form.note_category.data)
            note = Notes(note_name=form.note_name.data,
                         note_description=form.note_description.data,
                         note_content=filename,
                         user_id=current_user.id,
                         category=category,
                         category_id=category.category_id)
            db.session.add(category)
            db.session.add(note)
            db.session.commit()

            flash('Note Added', 'success')
    else:
        flash("The page you are trying to access is restricted", "danger")
        return redirect(url_for('index'))
    return render_template('notes_upload.html', form=form, title="Notes Upload")


@app.route('/video_upload', methods=['GET', 'POST'])
@login_required
def video_upload():
    form = UploadVideoForm()
    if session['username'] == 'Admin':
        if form.validate_on_submit():
            video_to_upload = request.files['video_content_']
            filename = str(uuid.uuid4()) + os.path.splitext(
                secure_filename(video_to_upload.filename))[1]
            video_to_upload.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            category = Category(category_name=form.video_category.data)
            video = Video(video_name=form.video_name.data,
                          video_description=form.video_description.data,
                          video_content=filename,
                          user_id=current_user.id,
                          category=category,
                          category_id=category.category_id
                          )
            db.session.add(category)
            db.session.add(video)
            db.session.commit()
            flash('Video Added', 'success')
    else:
        flash("The page you are trying to access is restricted", "danger")
        return redirect(url_for('index'))
    return render_template('video_upload.html', form=form, title="Video Upload")


@app.route('/info_upload', methods=['GET', 'POST'])
@login_required
def info_upload():
    form = UploadInfoForm()
    if session['username'] == 'Admin':
        if form.validate_on_submit():
            info_to_upload = request.files['info_image_']
            filename = str(uuid.uuid4()) + os.path.splitext(
                secure_filename(info_to_upload.filename))[1]
            info_to_upload.save(os.path.join(Config.UPLOAD_FOLDER_2, filename))
            info = Information(info_title=form.info_title.data,
                               info_description=form.info_description.data,
                               info_image=filename,
                               user_id=current_user.id)
            db.session.add(info)
            db.session.commit()

            flash('Information Added', 'success')
    else:
        flash("The page you are trying to access is restricted", "danger")
        return redirect(url_for('index'))
    return render_template('info_upload.html', form=form, title="Information Upload")


@app.route('/event_upload', methods=['GET', 'POST'])
@login_required
def event_upload():
    form = UploadEventForm()
    if session['username'] == 'Admin':
        if form.validate_on_submit():
            event_to_upload = request.files['event_image']
            filename = str(uuid.uuid4()) + os.path.splitext(
                secure_filename(event_to_upload.filename))[1]
            event_to_upload.save(os.path.join(Config.UPLOAD_FOLDER_3, filename))
            event = Events(event_title=form.event_title.data,
                           event_description=form.event_description.data,
                           event_image=filename,
                           start_date=form.start_date.data,
                           end_date=form.end_date.data,
                           user_id=current_user.id)
            db.session.add(event)
            db.session.commit()

            flash('Event Added', 'success')
    else:
        flash("The page you are trying to access is restricted", "danger")
        return redirect(url_for('index'))
    return render_template('event_upload.html', form=form, title="Event Upload")


@app.route('/upload_content')
@login_required
def upload_content():
    if session['username'] == 'Admin':
        return render_template('upload_content.html')
    else:
        flash('The page you are trying to access is restricted', 'danger')
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html', title='404 - Page Not Found'), 404


# View function for 500 error (internal server error)
@app.errorhandler(500)
def internal_server_error(err):
    return render_template('500.html', title='500 - Internal Server Error'), 500
