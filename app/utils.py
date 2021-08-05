from flask import url_for, redirect
from functools import wraps
from flask_login import current_user


def anonymous(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('main.playlists'))
        return f(*args, **kwargs)

    return decorated_function
