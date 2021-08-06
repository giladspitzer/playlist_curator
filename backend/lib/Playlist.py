from backend.lib.Person import Person
from backend.lib.Track import Track
import backend.api.calls as api
from pprint import pprint


class Playlist:
    id = ''
    name = ''
    description = ''
    img = ''
    collaborative = False
    owner = None
    public = False
    track_count = 0
    tracks = []

    def __init__(self, playlist_id, data=None):
        self.id = playlist_id
        if data is not None:
            self.apply_data(data)
        else:
            playlist_data = api.get_playlist(self.id)
            self.apply_data(playlist_data)


    def __repr__(self):
        return '<Playlist {}>'.format(self.name)

    def apply_data(self, data):
        self.name = data['name']
        self.description = data['description']
        self.img = data['images'][1]['url'] if len(data['images']) > 1 else data['images'][0]['url']
        self.collaborative = data['collaborative']
        self.owner = Person(login=False, e_user_id=data['owner']['id'], user_data=data['owner'])
        self.public = data['public']
        self.track_count = data['tracks']['total']

    def get_tracks(self):
        self.tracks = [Track(track['track']) for track in api.get_playlist_tracks(self.id)]

    def jsonify(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'img': self.img,
            'colab': self.collaborative,
            'owner': self.owner.jsonify(),
            'public': self.public,
            'tracks_total': self.track_count,
            'tracks': [track.jsonify() for track in self.tracks]
        }

