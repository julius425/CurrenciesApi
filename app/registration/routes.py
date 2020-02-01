import flask
from app import db, guard
from app.models import User
from app.registration import registration_blueprint as rbp
import json


@rbp.route('/signup', methods=['POST',])
def register():

    """
    Роут регистрации
    curl -X POST http://127.0.0.1:5000/accounts/signup \
        -d '{"username": "user", "password": "12345", "password2": "12345"}'

    Прирегистрации создается токен, который можно получить обратившийсь к /login    
    """

    request_data = flask.request.get_json(force=True)
    print(request_data)
    if not request_data:
        return 'Предоставьте данные в формате '\
                       '{"username":"user", "password":"12345", "password2":"12345}', 400

    username = request_data.get('username')
    password = request_data.get('password')
    password2 = request_data.get('password2')

    if not password == password2:
        return 'Пароли не совпадают.', 400

    user = User(username=username, password=guard.hash_password(password))
    db.session.add(user)
    db.session.commit()
    return f'Пользователь {username} успешно зарегистрирован.', 200


@rbp.route('/login', methods=['POST',])
def login():

    """
    Роут для получения ключа авторизации
       $ curl -X POST http://localhost:5000/login  \
         -d '{"username":"user", "password":"12345"}'
    """

    request_data = flask.request.get_json(force=True)
    if not request_data:
        return 'Предоставьте данные в формате '\
                       '{"username":"user","password":"12345",}', 400

    username = request_data.get('username')
    password = request_data.get('password')

    user = guard.authenticate(username, password)
    token = {'access_token': guard.encode_jwt_token(user)}
    return token, 200


    
