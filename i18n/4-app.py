#!/usr/bin/env python3
''' Basic Flask app and Babel setup, Get Locale from request
Parameterized templates, Force locale with URL parameter '''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' app Config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    ''' Determine best match with supported languages '''
    # Check if locale is specified in URL parameter
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Use accept_languages.best_match as fallback
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world() -> str:
    ''' Output templates '''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
