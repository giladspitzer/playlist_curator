import requests
from flask import session


def parse_response(resp):
    if resp.ok:
        return resp.json()
    else:
        return None


def get_user(e_user_id=None):
    if e_user_id is None:
        uri = f'https://api.spotify.com/v1/me'
    else:
        uri = f'https://api.spotify.com/v1/users/{e_user_id}'
    response = requests.get(uri, headers={"Authorization": f"Bearer {session['token']}"})
    return parse_response(response)
