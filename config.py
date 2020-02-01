import os

# url запроса котировок
CURR_BY_DATE_URL = f'http://www.cbr.ru/scripts/XML_daily.asp'

# ключ авторизации для тестирования приложения
EXAMPLE_AUTH = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODA1NjE2MjYsImV4cCI6MTYxMjA5NzYyNiwianRpIjoiYWE1ZTNhOGYtYjEzNC00YjcwLTljY2MtMDRlZGU0MTJkZTMyIiwiaWQiOjMsInJscyI6IiIsInJmX2V4cCI6MTYxMjA5NzYyNn0.zPg5b1nA3hEuKVh-jzB9cFUhMfiq8T3AriaTcRZXKS8'


class Config:

    """
    dev конфигурация
    """

    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BUNDLE_ERRORS = True
    SECRET_KEY = "test"
    JSON_AS_ASCII = False

    JWT_ACCESS_LIFESPAN = {'days': 365}
    JWT_REFRESH_LIFESPAN = {'days': 365}


class TestConfig(Config):

    """
    Тестовая конфигурация
    """

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True
    CSRF_ENABLED = False
    