from flask import Blueprint

registration_blueprint = Blueprint('registration', __name__)

from app.registration import routes