from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_bootstrap import Bootstrap4
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'postgresql://postgres:agrihandy*20@localhost/ibtdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
bootstrap = Bootstrap4(app)
moment = Moment(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db, render_as_batch=True)


from app import routes

