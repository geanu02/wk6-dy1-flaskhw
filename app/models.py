from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    password = db.Column(db.String)

    def __repr__(self):
        return f"Registered Email: {self.email}"

    def commit(self):
        db.session.add(self)
        db.session.commit()
