# coding: utf-8

from flask import (
    current_app
)
from flask.ext.login import UserMixin, current_user
from flask.ext.sqlalchemy import SQLAlchemy
from blinker import Namespace
from werkzeug.security import generate_password_hash, check_password_hash


user_signals = Namespace()
user_created = user_signals.signal('user_created')
user_deleted = user_signals.signal('user_deleted')


db = SQLAlchemy(current_app) if 'sqlalchemy' not in current_app.extensions else current_app.extensions.get('sqlalchemy').db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, unique=True, nullable=False)
    pw_hash = db.Column(db.String)
    activity = db.Column(db.Boolean, default=True, server_default='true')
    is_admin = db.Column(db.Boolean, default=False, server_default='false')

    @property
    def password(self):
        return self.pw_hash

    @password.setter
    def password(self, password):
        if password:
            self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
