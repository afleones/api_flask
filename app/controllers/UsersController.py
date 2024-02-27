# app/controllers/UsersController.py

from flask import request, jsonify
from app.models.User import User
from app import db

def registrar_usuario():
    # Verificar si la solicitud contiene datos JSON
    if request.is_json:
        # Obtener los datos JSON de la solicitud
        data = request.json

        # Crear una nueva instancia de User
        new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )

        # Agregar el nuevo usuario a la base de datos
        db.session.add(new_user)
        db.session.commit()

        # Devolver una respuesta JSON indicando éxito
        return jsonify({'message': 'User created successfully'}), 201
    else:
        # Devolver un error si la solicitud no contiene datos JSON
        return jsonify({'error': 'JSON data is required'}), 400
