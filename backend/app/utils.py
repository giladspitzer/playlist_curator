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


def get_redirect_uri(encoded=True):
    if encoded:
        return url_for('auth.callback', _external=True).replace(':', '%3A').replace('/', '%2F')
    else:
        return url_for('auth.callback', _external=True)


def get_api_scopes():
    scopes_string = 'user-read-private%20' \
                    'user-read-email%20' \
                    'user-read-recently-played%20' \
                    'user-read-playback-state%20' \
                    'user-top-read%20' \
                    'app-remote-control%20' \
                    'playlist-modify-public%20' \
                    'user-modify-playback-state%20' \
                    'playlist-modify-private%20' \
                    'user-follow-modify%20' \
                    'user-read-currently-playing%20' \
                    'user-follow-read%20' \
                    'user-library-modify%20' \
                    'user-read-playback-position%20' \
                    'playlist-read-private%20' \
                    'user-library-read%20' \
                    'playlist-read-collaborative%20' \
                    'streaming%20'
    return scopes_string
