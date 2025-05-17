from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema

main = Blueprint('main', __name__)

main.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@main.route('/')
def root():
    return {'mensaje': 'API Flask GraphQL activa. Ir a /graphql para usar la interfaz.'}
