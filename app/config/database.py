import os

class Database:
    DEBUG = os.getenv('DATABASE_DEBUG', False)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://root@localhost:3306/api_flask')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
