from flask import Blueprint, request
from app.controllers.UsersController import registrar_usuario
from app.controllers.IndexController import index

api = Blueprint('api', __name__)

@api.route('/')
def index_route():
    return index()

@api.route('/registro', methods=['POST'])
def registro():
    return registrar_usuario()


# Puedes agregar más rutas aquí para otras funcionalidades de tu API
