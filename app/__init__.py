import config
import flask_cors
import flask_praetorian
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, current_app
from flask_restful import Api


db = SQLAlchemy()
guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()


def create_app():

    
    app = Flask(__name__)
    api = Api(app)
    
    # Импортируем конфигурацию
    app.config.from_object('config.Config')

    
    # Инициализируем базу
    from app.models import User
    
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Инициализируем элементы авторизации
    guard.init_app(app, User)
    cors.init_app(app)

    # Создаем регистрацию по токенам
    from app.registration import registration_blueprint as rbp
    app.register_blueprint(rbp, url_prefix='/accounts')

    # Создаем эндпоинты 
    from app.endpoints.currency import CurrencyRetrieve

    api.add_resource(CurrencyRetrieve, '/cbr')

    return app


