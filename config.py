import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://DB 주소 비공개'


class ProductionConfig(Config):
    # Heroku DB
    SQLALCHEMY_DATABASE_URI = 'postgres://DB 주소 비공개'
