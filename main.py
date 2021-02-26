from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

import config 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key

# Whenever the admin panel is created

login = LoginManager()


# Assigns "db" to SQLAlchemy() for easier coding
db = SQLAlchemy()
import models


# Migration so we don't need to drop the table
migrate = Migrate(app, db, compare_type=True)
with app.test_request_context():
    db.init_app(app)
    db.create_all()

    login.init_app(app)

import src 
import webpanel
