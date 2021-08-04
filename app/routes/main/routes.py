from flask import request, redirect, session
from flask_login import login_user, current_user
from app.routes.main import bp
from app.models import User
from datetime import datetime, timedelta
from api.calls import get_user
import requests
from lib.Person import Person


@bp.route('/')
def hello_world():
    return redirect("https://accounts.spotify.com/authorize?client_id=***REMOVED***&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcallback&scope=user-read-private%20user-read-email%20&state=34fFs29kd09")


@bp.route('/callback')
def callback():
    callback_code = request.args.get('code')
    response = requests.post('https://accounts.spotify.com/api/token',
                             headers = {'Content-Type': 'application/x-www-form-urlencoded'},
                             auth=('***REMOVED***', '***REMOVED***'),
                             data={'grant_type': 'authorization_code',
                                   'redirect_uri': 'http://127.0.0.1:5000/callback',
                                   'code': callback_code}).json()
    token = response['access_token']
    session['token'] = token
    session['expiry'] = datetime.now() + timedelta(seconds=response['expires_in'])
    session['refresh_token'] = response['refresh_token']
    Person(login=True)
    return str('Logged in')


