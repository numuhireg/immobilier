import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/immobilier?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False