from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

from app import db, login


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String)
    fave_pokemon = db.relationship('FavePokemon', backref='Author', lazy=True)

    def __repr__(self):
        return f"Registered Email: {self.email}"

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password_input):
        return check_password_hash(self.password, password_input)

    def get_id(self):
        return str(self.user_id)


class FavePokemon(db.Model):
    fave_id = db.Column(db.Integer, primary_key=True)
    poke_num = db.Column(db.Integer)
    poke_name = db.Column(db.String(75))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return f"Pokemon # {self.poke_num}: {self.poke_name}"

    def commit(self):
        db.session.add(self)
        db.session.commit()
