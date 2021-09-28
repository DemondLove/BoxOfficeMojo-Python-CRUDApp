from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    # Why?
    config[config_name].init_app(app)

    db.init_app(app)

    from views import view
    app.register_blueprint(view)
    
    return app