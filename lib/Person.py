from flask import session
from flask_login import login_user
from api.calls import get_user
from app.models import User
from app import db

class Person:
    id = None
    name = ''
    country = ''
    email = ''
    e_id = ''
    other_data = {}

    def __repr__(self):
        return '<Person {}>'.format(self.name)

    def __init__(self, login=False, e_user_id=None, user_data=None):
        if user_data is None:
            user = get_user(e_user_id)
        else:
            user = user_data
        if user is not None:
            self.e_id = user['id']
            self.name = user['display_name']
            self.other_data = user
            if 'country' in user.keys():
                self.country = user['country']
            if 'email' in user.keys():
                self.email = user['email']

        if login:
            session['current_user_details'] = self
            base_q = db.session.query(User).filter(User.e_id == self.e_id)
            if base_q.count() == 0:
                new_user = User(e_id=str(self.e_id))
                db.session.add(new_user)
                db.session.commit()
            else:
                login_user(base_q.first())

    def jsonify(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'email': self.email,
            'e_id': self.e_id,
            'other_data': self.other_data
        }
