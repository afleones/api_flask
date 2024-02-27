from flask import Flask
import os
import sys

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/api_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Añade el directorio 'app' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

