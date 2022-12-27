from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(id):
   return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    program = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False, default='Kpelle Town')
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"User({self.full_name})"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Video(db.Model):
    __tablename__ = 'videos'
    video_id = db.Column(db.Integer, primary_key=True)
    video_name = db.Column(db.String(255), nullable=False)
    video_description = db.Column(db.String(300), nullable=False)
    video_content = db.Column(db.String(255), nullable=False, default='default.jpg')
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))

    def __repr__(self):
        return f"Video({self.video_name})"


class Notes(db.Model):
    __tablename__ = 'notes'
    note_id = db.Column(db.Integer, primary_key=True)
    note_name = db.Column(db.String(255), nullable=False)
    note_description = db.Column(db.String(300), nullable=False)
    note_content = db.Column(db.String(255), nullable=False, default='default.jpg')
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))

    def __repr__(self):
        return f"Notes({self.note_name})"


class Events(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(255), nullable=False)
    event_description = db.Column(db.String(300), nullable=False)
    event_image = db.Column(db.String(255), nullable=False, default='default.jpg')
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    from_time = db.Column(db.Time)
    to_time = db.Column(db.Time)
    registration_link = db.Column(db.String(255))
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Notes({self.note_name})"


class Information(db.Model):
    __tablename__ = 'information'
    info_id = db.Column(db.Integer, primary_key=True)
    info_title = db.Column(db.String(255), nullable=False)
    info_description = db.Column(db.String(300), nullable=False)
    info_image = db.Column(db.String(100), nullable=True, default='default.jpg')
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Information{self.info_title})"


class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Notes', backref='category')
    videos = db.relationship('Video', backref='category')

    def __repr__(self):
        return f"Category{self.category_name})"




