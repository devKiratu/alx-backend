#!/usr/bin/env python3
"""
Flask app with flask_babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app, default_timezone="UTC", default_locale="en")


class Config:
    """
    houses Babel configurations
    """
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


@app.route('/')
def index():
    """
    Flask app entry point for route /
    """
    return render_template('1-index.html')
