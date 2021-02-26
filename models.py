from main import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from main import login
import sqlalchemy


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class UserData(db.Model):
    discord_id = db.Column(db.String(32), primary_key=True, unique=True)
    background = db.Column(db.String(32))
    overlay = db.Column(db.String(32))


class User(db.Model, UserMixin):
    # Used to login to the Admin Panel
    id = db.Column(db.Integer, primary_key=True, default=1)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


