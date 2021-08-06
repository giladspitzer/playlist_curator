from flask import request, redirect, session, url_for, current_app
from flask_login import login_required, current_user
from backend.app.routes.auth import bp
from backend.app.utils import anonymous, get_redirect_uri, get_api_scopes
from datetime import datetime, timedelta
from backend.api.calls import get_token
from backend.lib.Person import Person


@bp.route('')
def login():
    if current_user.is_authenticated:
        return redirect('/')
    else:
        return redirect(f"https://accounts.spotify.com/authorize?"
                        f"client_id={current_app.config['SPOTIFY_API_KEY']}&"
                        f"response_type=code&"
                        f"redirect_uri={get_redirect_uri(True)}&"
                        f"scope={get_api_scopes()}&"
                        f"state=34fFs29kd09"
                        )


@bp.route('/callback')
@anonymous
def callback():
    callback_code = request.args.get('code')
    response = get_token(callback_code, refresh=False)
    session['token'] = response['access_token']
    session['expiry'] = datetime.now() + timedelta(seconds=response['expires_in'])
    session['refresh_token'] = response['refresh_token']
    Person(login=True)
    return redirect('/')
