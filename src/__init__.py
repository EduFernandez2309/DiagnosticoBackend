from flask import Flask
from .routes import ProyectoRoutes, TipoProyectoRoutes
from flask_cors import CORS

app = Flask(__name__)

def register_blueprints(app):
    app.register_blueprint(ProyectoRoutes.main, url_prefix='/api/proyectos')
    app.register_blueprint(TipoProyectoRoutes.main, url_prefix='/api/tipo-proyecto')

def init_app(config):
    app.config.from_object(config)
    register_blueprints(app)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
    return app
