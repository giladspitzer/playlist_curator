from flask import Flask, redirect, url_for, session as flask_session
from flask_login import LoginManager, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from config import Config
from datetime import datetime, timedelta
from api.calls import get_token

login = LoginManager()  # creates status var for state of login
login.login_view = "main.main"
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

    @application.before_request
    def before_request():
        if current_user.is_authenticated:
            if flask_session.get('expiry') <= datetime.now():
                if flask_session.get('refresh_token') is not None:
                    response = get_token(flask_session.get('refresh_token'), refresh=True)
                    if response is not None:
                        flask_session['token'] = response['access_token']
                        flask_session['expiry'] = datetime.now() + timedelta(seconds=response['expires_in'])
                        flask_session['refresh_token'] = None
                    else:
                        pass
                else:
                    flask_session.clear()
                    logout_user()
                    return redirect(url_for('main.main'))
        else:
            flask_session.clear()

    return application


from app import models
