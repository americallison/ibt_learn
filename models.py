from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


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
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"User({self.full_name})"


class Video(db.Model):
    __tablename__ = 'videos'
    video_id = db.Column(db.Integer, primary_key=True)
    video_name = db.Column(db.String(255), nullable=False)
    video_description = db.Column(db.String(300), nullable=False)
    video_content = db.Column(db.String(255), nullable=False, default='default.jpg')
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

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

    def __repr__(self):
        return f"User({self.note_name})"


class Information(db.Model):
    __tablename__ = 'information'
    info_id = db.Column(db.Integer, primary_key=True)
    info_title = db.Column(db.String(255), nullable=False)
    info_description = db.Column(db.String(300), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"User({self.info_title})"



