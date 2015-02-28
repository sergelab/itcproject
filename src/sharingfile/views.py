# coding: utf-8

from flask import (
    Blueprint,
    current_app,
    render_template,
    redirect,
    url_for,
    request,
    flash
)
from flask.ext.login import (
    login_required,
    current_user,
    login_user,
    logout_user
)
from flask.ext.babel import gettext as _
from flask.ext.assets import Bundle
from .forms import LoginForm
from itc.init import assets


bp = Blueprint('sharingfile', __name__, template_folder='templates', static_folder='static', url_prefix='/sharing')

current_app.login_manager.login_view = 'sharingfile.login'
current_app.login_manager.session_protection = 'base'


@bp.route('/')
@login_required
def index():
    print(current_user)
    return render_template('sharingfile/main.html')


@bp.route('/users')
@login_required
def users():
    pass


@bp.route('/users/add', methods=['GET', 'POST'])
@bp.route('/users/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id=None):
    pass


@bp.route('/files')
@login_required
def files():
    pass


@bp.route('/files/add', methods=['GET', 'POST'])
@bp.route('/files/<int:file_id>', methods=['GET', 'POST'])
@login_required
def edit_file():
    pass


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('index'))

    form = LoginForm() if request.method == 'POST' else LoginForm(request.args)

    if form.validate_on_submit():
        if login_user(form.user) is True:
            flash(_('Logged in successfully message'))
        else:
            flash(_('Logging failed message'))

        return redirect(form.next.data or url_for('sharingfile.index'))

    return render_template('sharingfile/login.html',
                           form=form
                          )


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(request.args.get('next') or url_for('sharingfile.login'))


assets.register('css_sf', Bundle(
    'sharingfile/css/uikit.css',
    'sharingfile/css/uikit.gradient.css',
    'sharingfile/css/common.css',
    filters='jinja2',
    output='css/sharingfile.css'
))


assets.register('js_sf', Bundle(
    'sharingfile/js/jquery.js',
    'sharingfile/js/uikit.js',
    'sharingfile/js/common.js',
    filters='jinja2',
    output='js/sharingfile.js'
))
