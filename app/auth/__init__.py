from flask import Blueprint
# set the prefix por url

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views