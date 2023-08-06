#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """check the 'lang' parameter in the url
    """
    locale = request.args.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale
    """ if no 'lang' parameter use default Flask-Babel
        local selector
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user(user_id):
    """ get user id """
    return users.get(user_id)


@app.before_request
def before_request():
    """ set user id as global """
    user_id = request.args.get("login_as")
    if user_id:
        user_id = int(user_id)
        g.user = get_user(user_id)
    else:
        g.user = None


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
