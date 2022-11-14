import os


# create Config class to store settings
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'j*9)a$#@$Tyjg$#<,Hag)ll8#49#@!()'
    UPLOAD_FOLDER = 'app/static/videos/'
    UPLOAD_FOLDER_1 = 'app/static/notes/'
    UPLOAD_FOLDER_2 = 'app/static/information/'
    MAX_CONTENT_LENGTH = 200 * 1024 * 1024
    SQLALCHEMY_TRACK_MODIFICATIONS = False