#!/usr/bin/env python3
"""
Flask app with flask_babel setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Flask app entry point for route /
    """
    return render_template('5-index.html', user=g.user)
