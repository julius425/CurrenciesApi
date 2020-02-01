Описание 
==================
Прокси-api приложение предоставляющее клиенту котировки от стороннего REST сервиса.

*   Бэкенд - Flask, Flask_REST, Flask_Praetorian 


Установка
===========
1.  Качаем :
    `git clone https://github.com/julius425/CurrenciesApi.git`
2.  Настраиваем flask :
    1.  Переходим в папку:
        * `cd CurrenciesApi`
    2.  Включаем virtualenv и устанавливаем зависимости:
        * `veirtualenv -p python3.6 venv`
        * `. venv/bin/activate`
        * `pip install -r requirements.txt`
    3.  Экспортируем переменную среды фласка:
        * `export FLASK_APP=api.py`    
3. Запускаем проект:
   `python api.py`
4. Пользуемся(например curl'ом):
    1.  Регистрируемся в приложении(лог\пас уже есть в базе, можно переходить к п.3):
        * `curl -X POST http://127.0.0.1:5000/accounts/signup -d '{"username": "admin123", "password": "admin123", "password2": "admin123"}'` 
    2.  Логинимся, получаем токен авторизации:
        * `curl -X POST http://127.0.0.1:5000/accounts/login -d '{"username": "admin123","password":"admin123"}'`
    3.  Запрашиваем данные у стороннего сервиса:
        * `curl -X GET http://127.0.0.1:5000/cbr -H "Content-type: application/json; charset=utf-8" -H "Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODA1NjE2MjYsImV4cCI6MTYxMjA5NzYyNiwianRpIjoiYWE1ZTNhOGYtYjEzNC00YjcwLTljY2MtMDRlZGU0MTJkZTMyIiwiaWQiOjMsInJscyI6IiIsInJmX2V4cCI6MTYxMjA5NzYyNn0.zPg5b1nA3hEuKVh-jzB9cFUhMfiq8T3AriaTcRZXKS8" -d '{"date_req": "02/03/2002"}'`   
