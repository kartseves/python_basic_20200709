"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""

str_bad_input = 'Некорректный ввод значения.'
str_zero_division = 'На ноль делить нельзя!'
str_question1 = 'Введите делимое: '
str_question2 = 'Введите делитель: '
str_answer = 'Результат деления:'


def divide(p_1=0, p_2=1):
    """Возвращает частное от деления.
    Именованные параметры:
    p_1 -- делимое (по умолчанию 0.0)
    p_2 -- делитель (по умолчанию 1.0)
    """
    return p_1/p_2


while True:
    user_input = input(str_question1)
    try:
        dividend = abs(int(user_input))
        break
    except ValueError as error:
        print(str_bad_input)
        continue

while True:
    user_input = input(str_question2)
    try:
        print(f"{str_answer} {divide(dividend, int(user_input))}")
    except ValueError as error:
        print(str_bad_input)
        continue
    except ZeroDivisionError as error:
        print(str_zero_division)
        continue
    break
