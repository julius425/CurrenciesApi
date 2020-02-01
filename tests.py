# from datetime import datetime, timedelta
import unittest
import config
from unittest.mock import patch, Mock
from app import create_app, db
from app.models import User, Record
from flask_restful import Resource
import requests
import json
from app.endpoints.currency import cbr_request_by_date


class AppFunctionalityTest(unittest.TestCase):

    """
    Тестируем:
    -создание пользователя
    -входящий запрос с авторизацией
    -исходящий запрос на внешний сервис
    """

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object('config.TestConfig')
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def call_remote(self, date):
        response = cbr_request_by_date(date)
        return response

    def test_user(self):

        """
        Тестируем создание модели юзера и записи его запроса 
        """

        data = '/sample'
        username = 'testuser'
        password = 'password'
        
        u = User(username=username, password=password)
        db.session.add(u)
        r = Record(record_uri=data, user_id=1)
        db.session.add(r)

        db.session.commit()

        self.created_user = User.query.filter_by(username='testuser').first()
        created_user_record = self.created_user.records.first().record_uri
    

        assert self.created_user is not None
        self.assertEqual(self.created_user.username, username)
        self.assertEqual(created_user_record, data)
    
    def test_inc_request(self):

        """
        Тестируем входящий от пользователя запрос
        """

        headers = {
            'Content-type': 'application/json',  
            'Accept': 'text/plain',
            'Content-Encoding': 'utf-8',
            'Authorization': f'Bearer {config.EXAMPLE_AUTH}'
        }

        data = {"date_req": "02/03/2002"}
    
        response = self.client().get('/cbr', data=json.dumps(data), headers=headers)
        self.assertEqual(str(response), '<Response streamed [200 OK]>')

    @patch('app.endpoints.currency.cbr_request_by_date')
    def test_vacancies_request(self, mock_cbr_request_by_date):

        """
        Тестируем исходящий от приложения в сторону сервиса запрос 
        """

        mock_status_200 = Mock(status_code=200)
        mock_status_200.json.return_value = [{
            "request": "success"
        }]
        mock_cbr_request_by_date.return_value = mock_status_200

        response =  self.call_remote({"date":"date"})

        self.assertEqual(response.status_code, 200)    


if __name__ == '__main__':
    unittest.main(verbosity=2)