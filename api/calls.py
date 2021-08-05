import requests
from flask import session


def parse_response(resp):
    if resp.ok:
        return resp.json()
    else:
        print('Error')
        print(resp.text)
        return None


def get_token(code, refresh=False):
    if not refresh:
        response = parse_response(requests.post('https://accounts.spotify.com/api/token',
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                 auth=('***REMOVED***', '***REMOVED***'),
                                 data={'grant_type': 'authorization_code',
                                       'redirect_uri': 'http://127.0.0.1:5000/callback',
                                       'code': code}))

    else:
        response = parse_response(requests.post('https://accounts.spotify.com/api/token',
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                 auth=('***REMOVED***', '***REMOVED***'),
                                 data={'grant_type': 'refresh_token',
                                       'refresh_token': code}))
    return response


def get_user(e_user_id=None):
    if e_user_id is None:
        uri = f'https://api.spotify.com/v1/me'
    else:
        uri = f'https://api.spotify.com/v1/users/{e_user_id}'
    response = requests.get(uri, headers={"Authorization": f"Bearer {session['token']}"})
    return parse_response(response)


def get_playlists():
    more = True
    playlists = []
    uri = 'https://api.spotify.com/v1/me/playlists'
    while more:
        resp = requests.get(uri, headers={"Authorization": f"Bearer {session['token']}"})
        playlists.extend(resp.json()['items'])
        if resp.json()['next'] is not None:
            uri = resp.json()['next']
        else:
            more = False
    return playlists


def get_playlist(playlist_id):
    resp = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}',
                        headers={"Authorization": f"Bearer {session['token']}"})

    return parse_response(resp)


def get_playlist_tracks(playlist_id):
    more = True
    tracks = []
    uri = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    while more:
        resp = requests.get(uri, headers={"Authorization": f"Bearer {session['token']}"})
        tracks.extend(resp.json()['items'])
        if resp.json()['next'] is not None:
            uri = resp.json()['next']
        else:
            more = False
    return tracks
