import os
import urllib
from sqlalchemy import create_engeni

class Config(object):
    SECRET_KEY = 'Clave_Nueva'
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://usuario:contrasenia@127.0.0.1/prueba'
    SQLALCHEMY_TRACK_MODIFICATION = False