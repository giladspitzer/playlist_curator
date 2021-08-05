
class Album:
    id = ''
    name = ''
    img = ''

    def __repr__(self):
        return '<Album {}>'.format(self.name)

    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.img = data['images'][1]['url']

    def jsonify(self):
        return {
            'id': self.id,
            'name': self.name,
            'img': self.img
        }
