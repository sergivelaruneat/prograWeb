from flask_cors import CORS
from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configuración de CORS ya que no estaba dando problemas con el frontend
    CORS(app)
    
    # Importacion de rutas
    from .routes import main
    app.register_blueprint(main)

    return app