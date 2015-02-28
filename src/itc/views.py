# coding: utf-8

from flask import render_template
from sharingfile.models import User
from .init import app, db, lm


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(401)
def not_authorized(error):
    return render_template('401.html', error=error), 401


@app.errorhandler(404)
def error_404(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def error_500(error):
    return render_template('500.html', error=error), 500


@app.errorhandler(501)
def not_implemented(error):
    return render_template('501.html', error=error), 501


@lm.user_loader
def load_user(user_id):
    try:
        user = User.query.filter(User.id == user_id, User.activity == True).first()
        return user
    except Exception as e:
        db.session.rollback()
        current_app.logger.exception(e)
