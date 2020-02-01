import flask
import requests
import config
from datetime import datetime
from app import db, guard
from app.models import Record
from flask import current_app
from flask_restful import Resource
from flask_praetorian import (
    auth_required,
    current_user,
    current_user_id
)




def cbr_request_by_date(date):

    """
    Делаем запрос в сторону cbr
    Формат входящей даты '{"date_req": "02/03/2002"}'
    """
    
    if date:
        response = requests.get(config.CURR_BY_DATE_URL + f'?date_req={date}')
    else:
        response = requests.get(config.CURR_BY_DATE_URL)
    return response


def make_log_string(r_data, code):

    """
    Логируем запрос, создаем запись в базу
    """

    r_uid = current_user_id()
    
    r_addr = flask.request.environ['REMOTE_ADDR']
    r_uri = flask.request.environ['REQUEST_URI']
    r_time = str(datetime.now())
    
    record_string = f"""
    ===========================
        Request info: 
        time: {r_time} 
        remote address: {r_addr}
        uri: {r_uri}
        user id: {r_uid}
        data: {r_data}
        host response: {code}
    ===========================    
    """

    Record.create_record(
        app=current_app,
        db=db,
        record_uri=r_uri,
        user_id=r_uid,
    )

    return record_string



class CurrencyRetrieve(Resource):

    @auth_required
    def get(self, **kwargs):

        """
        Эндпоинт перенаправляющий запрос в сторону удаленного сервиса
        """

        try:
            r_data = flask.request.get_json(force=True)
            date_req = r_data.get('date_req')
        except:
            r_data = None
            date_req = 'no date'

        response = cbr_request_by_date(date_req)
        record_string = make_log_string(r_data, response.status_code)

        print(record_string)

        return response.text

