from flask import Flask, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from config import Config

login = LoginManager()  # creates status var for state of login
db = SQLAlchemy()
migrate = Migrate()
session = Session()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(config_class)
    login.init_app(application)
    db.init_app(application)
    migrate.init_app(application, db)
    session.init_app(application)

    from app.routes.main import bp as main_bp
    application.register_blueprint(main_bp)

    return application


from app import models
