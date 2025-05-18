from flask import Flask
from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema

main = Blueprint('main', __name__)

#Ruta principal de la API
main.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # habilita la interfaz de usuario de GraphiQL
    )
)

# Ruta para cuan do se accede a la raiz /.
@main.route('/')
def index():
    return "Bienvenido a la API de la aplicación de gestión de tareas. Puedes acceder a la documentación en /graphql."