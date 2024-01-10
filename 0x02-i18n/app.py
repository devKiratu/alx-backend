#!/usr/bin/env python3
"""
Flask app with flask_babel setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
from datetime import datetime


class Config:
    """
    houses Babel configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    user dictionary or None if the ID cannot be found or
    if login_as was not passed
    """
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """
    executed before a request is processed
    """
    try:
        user = get_user()
        g.user = user
    except Exception:
        g.user = None


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages
    """
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Locale from user settings
    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    # Locale from request header
    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Infer appropriate time zone
    """
    # Find timezone parameter in URL parameters
    tzone = request.args.get('timezone')
    if tzone:
        try:
            return str(pytz.timezone(tzone))
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Find time zone from user settings
    if g.user:
        tzone = g.user.get('timezone')
        try:
            return str(pytz.timezone(tzone))
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """
    Flask app entry point for route /
    """
    curr_time = datetime.now(pytz.timezone(get_timezone()))
    return render_template('index.html', user=g.user,
                           current_time=format_datetime(curr_time))
