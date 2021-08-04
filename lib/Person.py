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

    def __init__(self, login=False):
        user = get_user()
        print(user)
        if user is not None:
            self.name = user['display_name']
            self.country = user['country']
            self.email = user['email']
            self.e_id = user['id']
            self.other_data = user
        if login:
            session['current_user_details'] = self
            base_q = db.session.query(User).filter(User.e_id == self.e_id)
            if base_q.count() == 0:
                new_user = User(e_id=str(self.e_id))
                db.session.add(new_user)
                db.session.commit()
            else:
                login_user(base_q.first())
