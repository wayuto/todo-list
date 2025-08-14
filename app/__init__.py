from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(
        __name__,
        static_folder=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "..", "static"
        ),
        template_folder=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "..", "templates"
        ),
    )
    app.config.from_object(config_class)

    db.init_app(app)

    from app import routes

    app.register_blueprint(routes.bp)

    return app
