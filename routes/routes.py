# routes/route.py
from flask import Blueprint, request
from app.controllers.IndexController import index

route = Blueprint('routes', __name__)

@route.route('/')
def index_route():
    return index()
