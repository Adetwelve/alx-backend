#!/usr/bin/env python3
""" Create a get_locale function with the babel.localeselector decorator """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
""" Replace 'en' and 'fr' with your deired
    language and their respective locales
"""
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ function that get local language """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ return an html file """
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run()
