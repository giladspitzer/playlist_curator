from backend.lib.Album import Album
from backend.lib.Artist import Artist

class Track:
    id = ''
    name = ''
    artists = []
    album = None
    preview_url = ''
    popularity = ''
    track_number = 0
    duration = 0  # ms
    explicit = False

    def __repr__(self):
        return '<Track {}>'.format(self.name)

    def __init__(self, track_data):
        print(track_data)
        self.id = track_data['id']
        self.name = track_data['name']
        self.preview_url = track_data['preview_url']
        self.popularity = track_data['popularity']
        self.duration = track_data['duration_ms']
        self.explicit = track_data['explicit']
        self.track_number = track_data['track_number']
        self.album = Album(track_data['album'])
        self.artists = [Artist(artist) for artist in track_data['artists']]

    def jsonify(self):
        return {
            'id': self.id,
            'name': self.name,
            'preview_url': self.preview_url,
            'popularity': self.popularity,
            'duration': self.duration,
            'explicit': self.explicit,
            'track_number': self.track_number,
            'album': self.album.jsonify() if self.album is not None else None,
            'artists': [artist.jsonify() for artist in self.artists]
        }
