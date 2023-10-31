#!/usr/bin/env python3

"""
"""
app = __import__("0-app").app
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """
    Configures available languages
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def index():
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
