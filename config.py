import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    # TODO : sqlite 말고 다른 DB
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///dev_db.sqlite3'


class ProductionConfig(Config):
    # TODO : sqlite 말고 다른 DB
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///prod_db.sqlite3'
