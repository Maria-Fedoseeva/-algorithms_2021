from binascii import hexlify
from hashlib import pbkdf2_hmac


class UserData:
    def __init__(self, new_login, new_pass: str):
        self.login = new_login.lower()
        password_hash = pbkdf2_hmac(hash_name='sha256',
                                    password=new_pass.encode(),
                                    salt=self.login.encode(),
                                    iterations=100000)
        self._password_hash = hexlify(password_hash)

    def authorization(self, password):
        chech_password = pbkdf2_hmac(hash_name='sha256',
                                     password=password.encode(),
                                     salt=self.login.encode(),
                                     iterations=100000)
        if self._password_hash == hexlify(chech_password):
            print('Вы ввели правильный пароль')
        else:
            print('Вы ввели неправильный пароль')


login = input('Введите логин: ')
password = input('Введите пароль: ')
user_1 = UserData(login, password)

print(f'В базе данных хранится строка: {user_1._password_hash}')
auth_pass = password = input('Введите пароль еще раз для проверки: ')
user_1.authorization(auth_pass)