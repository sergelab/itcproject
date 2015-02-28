# coding: utf-8

from flask.ext.babel import gettext as _, lazy_gettext as __
from flask.ext.wtf import Form as secureForm
import wtforms as wtf
from .models import User


class Form(secureForm):
    TIME_LIMIT = 360000


class WidgetPrebind(object):
    def __init__(self, widget, **kwargs):
        self.widget = widget
        self.kw = kwargs

    def __call__(self, field, **kwargs):
        return self.widget.__call__(field, **dict(self.kw, **kwargs))


class LoginForm(Form):
    login = wtf.TextField(__('Login label'),
                          validators=[wtf.validators.Required(__('Please, provide your login message'))],
                          widget=WidgetPrebind(wtf.widgets.TextInput(),
                                               class_='uk-width-1-1 uk-form-large',
                                               placeholder=__('Login placeholder'),
                                               size=30
                                              )
                         )
    password = wtf.PasswordField(__('Password label'),
                                 validators=[wtf.validators.Required()],
                                 widget=WidgetPrebind(wtf.widgets.PasswordInput(),
                                                      class_='uk-width-1-1 uk-form-large',
                                                      placeholder=__('Password placeholder'),
                                                      size=30,
                                                      autocomplete='off'
                                                     )
                                )
    remember_me = wtf.BooleanField(__('Remember me label'), default=False)
    next = wtf.HiddenField()

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter(User.login == self.login.data, User.activity == True).first()

        if not user or not user.check_password(self.password.data):
            self.errors.update({'form': [__('Invalid username or password message')]})
            return False

        self.user = user
        return True
