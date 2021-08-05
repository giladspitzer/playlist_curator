from flask import request, redirect, session, url_for
from flask_login import login_required, current_user
from app.routes.main import bp
from app.utils import anonymous
from datetime import datetime, timedelta
from api.calls import get_playlists, get_playlist_tracks, get_token
import requests
from lib.Person import Person
from lib.Playlist import Playlist
from pprint import pprint

@bp.route('/')
def main():
    if current_user.is_authenticated:
        return redirect(url_for('main.playlists'))
    else:
        return redirect("https://accounts.spotify.com/authorize?client_id=***REMOVED***&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcallback&scope=user-read-private%20user-read-email%20&state=34fFs29kd09")


@bp.route('/callback')
@anonymous
def callback():
    callback_code = request.args.get('code')
    response = get_token(callback_code, refresh=False)
    session['token'] = response['access_token']
    session['expiry'] = datetime.now() + timedelta(seconds=response['expires_in'])
    session['refresh_token'] = response['refresh_token']
    Person(login=True)
    return str('Logged in')


@bp.route('/playlists')
@login_required
def playlists():
    playlists = [Playlist(i['id'], i) for i in get_playlists()]
    return str([playlist.jsonify() for playlist in playlists])


@bp.route('/playlist/<id>')
@login_required
def playlist(id):
    playlist = Playlist(id)
    return str(playlist.jsonify())


@bp.route('/playlist/<id>/tracks')
@login_required
def playlist_tracks(id):
    playlist = Playlist(id)
    playlist.get_tracks()
    return str(playlist.jsonify())
