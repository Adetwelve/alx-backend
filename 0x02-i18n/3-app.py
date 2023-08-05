#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)

# Configure Babel
babel = Babel(app)

# Configure translations directory
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def index():
    # Use the 'gettext' function to get the translated strings
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world!")
    return render_template('3-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    app.run()
