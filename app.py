from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.database import Database
from dotenv import load_dotenv
from flask import Blueprint, request
from routes.api import api  # Importa desde routes/api.py
from routes.routes import route  # Importa desde routes/routes.py
import os
import sys

def before_request():
    if request.json is not None:
        request.data = request.json

app = Flask(__name__, template_folder='app/views')

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app.config.from_object(Database)

app.register_blueprint(api, url_prefix='/api')  # Usa el Blueprint 'api' desde routes/api.py
app.register_blueprint(route)  # Usa el Blueprint 'route' desde routes/route.py

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql://root@localhost:3306/api_flask')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Añade el directorio 'app' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

# Configuración de la base de datos y modelos
db = SQLAlchemy(app)

# Debes importar los modelos después de inicializar SQLAlchemy
from app.models.User import User

migrate = Migrate(app, db)

# Debes llamar a db.create_all() dentro del contexto de la aplicación Flask
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
