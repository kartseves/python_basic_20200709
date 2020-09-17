"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def print_user_data_1(name, surname, birth_year, city, email, tel_num):
    """Возвращает данные о пользователе одной строкой.
    Именованные параметры:
    name -- имя
    surname -- фамилия
    birth_year -- год рождения
    city -- город проживания
    email -- почта
    tel_num - телефон
    """
    print(name, surname, birth_year, city, email, tel_num, sep=', ')


def print_user_data_2(**kwargs):
    key_list = ('name', 'surname', 'birth_year', 'city', 'email', 'tel_num')
    result = ''
    for key in key_list:
        try:
            result += str(kwargs[key]) + ', '
        except KeyError as err:
            result += '<not found>, '
    print(result[:-2])


print_user_data_1(email='user@mail.ru', birth_year=1980, surname='Иванов', name='Иван', tel_num='333-333', city='Омск')
print_user_data_2(email='user@mail.ru', birth_year=1980, surname='Иванов', name='Иван', tel_num='333-333', city='Омск')
