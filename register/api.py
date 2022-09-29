# register/api.py

import requests

class Register:
    """
    Класс для работы с апи регистрации пользователя
    """
    def __init__(self, url):
        self.url = url

    POST_REGISTER_USER = '/register'

    def register_user(self, body: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser
        :param body: Принимает {"username": "mail", "password": "Password"}
        :return: Регистрирует пользователя
        """
        return requests.post(f'{self.url}{self.POST_REGISTER_USER}', json=body)
