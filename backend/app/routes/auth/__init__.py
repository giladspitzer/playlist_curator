from flask import Blueprint


bp = Blueprint('auth', __name__)


from backend.app.routes.auth import routes
