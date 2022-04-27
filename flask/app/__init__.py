"""
Main Flask app file
"""

import dotenv
from app.blueprints.open import bp_open
from app.blueprints.api import bp_api
from flask import Flask


def create_app():
    """
    Factory funtion for flask
    returns: app object
    """
    _app = Flask(__name__)
    _app.config.from_pyfile('settings.py')

    _app.register_blueprint(bp_open)
    _app.register_blueprint(bp_api, url_prefix='/api/v1.0')

    return _app

dotenv.load_dotenv()
app = create_app()
