import os
from settings import *

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DEV_DB_URI


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = PROD_DB_URI
