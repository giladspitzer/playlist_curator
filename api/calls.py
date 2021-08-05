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
    response = requests.get('https://api.spotify.com/v1/me/playlists', headers={"Authorization": f"Bearer {session['token']}"})
    return parse_response(response)


def get_playlist_tracks(playlist_id):
    response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers={"Authorization": f"Bearer {session['token']}"})
    return parse_response(response)
