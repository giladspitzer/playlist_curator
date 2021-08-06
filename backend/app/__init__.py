from flask import Flask, redirect, url_for, session as flask_session, render_template
from flask_login import LoginManager, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from backend.config import Config
from datetime import datetime, timedelta
from backend.api.calls import get_token
import os

login = LoginManager()  # creates status var for state of login
login.login_view = "auth.login"
db = SQLAlchemy()
migrate = Migrate()
session = Session()


def create_app(config_class=Config):
    template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir = os.path.join(template_dir, 'frontend')
    template_dir = os.path.join(template_dir, 'dist')

    application = Flask(__name__, template_folder=template_dir, static_folder=template_dir, static_url_path='/')
    application.config.from_object(config_class)
    login.init_app(application)
    db.init_app(application)
    migrate.init_app(application, db)
    session.init_app(application)
    print(application.static_url_path, application.has_static_folder, application.static_folder)
    from backend.app.routes.main import bp as main_bp
    application.register_blueprint(main_bp, url_prefix='/api')
    from backend.app.routes.auth import bp as auth_bp
    application.register_blueprint(auth_bp, url_prefix='/api/auth')

    @application.before_request
    def before_request():
        print(url_for('auth.callback', _external=True,))
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
                    return redirect(url_for('auth.login'))
        else:
            flask_session.clear()

    @application.route('/')
    def template():
        return render_template('index.html')

    return application


from backend.app import models
