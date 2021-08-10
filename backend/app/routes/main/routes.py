from flask import request, redirect, session, url_for, current_app, jsonify
from flask_login import login_required
from backend.app.routes.main import bp
from backend.api.calls import get_playlists
from backend.lib.Playlist import Playlist



@bp.before_request
@login_required
def before_request():
    pass


@bp.route('/playlists')
def playlists():
    playlists = [Playlist(i['id'], i) for i in get_playlists()]
    return jsonify([playlist.jsonify() for playlist in playlists])


@bp.route('/playlist/<id>')
def playlist(id):
    playlist = Playlist(id)
    return str(playlist.jsonify())


@bp.route('/playlist/<id>/tracks')
def playlist_tracks(id):
    playlist = Playlist(id)
    playlist.get_tracks()
    return str(playlist.jsonify())
