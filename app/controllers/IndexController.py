from flask import render_template

def index():
    title = 'Página de inicio'
    greeting = '¡Hola, mundo!'
    content = 'Bienvenido a mi aplicación Flask.'
    return render_template('index.html', title=title, greeting=greeting, content=content)