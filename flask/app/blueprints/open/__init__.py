"""
Open HTML blueprint
"""
from flask import Blueprint, render_template

bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    """
    Index route
    returns: index.html
    """
    return render_template('index.html')
