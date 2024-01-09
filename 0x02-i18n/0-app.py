#!/usr/bin/env python3
"""
Entry point for flask app to demonstrate i18n
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Serves route /
    """
    return render_template('0-index.html')
