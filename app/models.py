from flask_login import UserMixin
from app import db, login
from sqlalchemy import func


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    e_id = db.Column(db.String(120), index=True, unique=True)

    inserted_at = db.Column(db.DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return '<User {}>'.format(self.id)

