from flask import request, redirect, session
from flask_login import login_required
from app.routes.main import bp
from app.models import User
from datetime import datetime, timedelta
from api.calls import get_playlists, get_playlist_tracks, get_token
import requests
from lib.Person import Person
from pprint import pprint

@bp.route('/')
def main():
    return redirect("https://accounts.spotify.com/authorize?client_id=***REMOVED***&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcallback&scope=user-read-private%20user-read-email%20&state=34fFs29kd09")


@bp.route('/callback')
def callback():
    callback_code = request.args.get('code')
    response = get_token(callback_code, refresh=False)
    session['token'] = response['access_token']
    session['expiry'] = datetime.now() + timedelta(seconds=5)
    session['refresh_token'] = response['refresh_token']
    Person(login=True)
    return str('Logged in')


@bp.route('/playlists')
@login_required
def playlists():
    response = get_playlists()
    text = ''
    for i in response['items']:
        text += '\n'
        text += i['name']
        # tracks = get_playlist_tracks(i['id'])['items']
        # for j in tracks:
        #     print('-------')
        #     pprint(j['track'])
    return str(text)

