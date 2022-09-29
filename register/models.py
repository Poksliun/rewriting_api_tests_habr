# register/models
from faker import Faker

fake = Faker()

class RegisterUser:
    # Декоратор позволяющий использовать статический метод
    # (то есть нам не обязательно создавать экхемпляр)
    @staticmethod
    def Random():
        # Генерирует меил и пароль
        username = fake.email()
        password = fake.password()
        return {'username': username, 'password': password}

