from flask import Flask
from flask_cors import CORS
from app.config import Config

def create_app():
    # Crear una instancia de la aplicación Flask
    app = Flask(__name__)
    # Cargar la configuración de la aplicación desde la clase Config
    app.config.from_object(Config)
    # Habilitar CORS para la aplicación
    CORS(app)
    # Importar el blueprint api_bp desde app.routes
    from app.routes import api_bp
    # Registrar el blueprint api_bp en la aplicación con la URL base /api/v1
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    return app
