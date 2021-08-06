
class Artist:
    id = ''
    name = ''

    def __repr__(self):
        return '<Artist {}>'.format(self.name)

    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']

    def jsonify(self):
        return {
            'id': self.id,
            'name': self.name,
        }
