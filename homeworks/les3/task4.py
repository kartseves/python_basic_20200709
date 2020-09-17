"""
4. Программа принимает действительное положительное число x и целое
отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

str_bad_input = 'Некорректный ввод значения.'
str_question1 = 'Введите действительное положительное число x: '
str_question2 = 'Введите целое отрицательное число y: '
str_answer = 'Результат возведения числа x в степень y:'


def my_extent_1(a: float, b: int):
    """Возвращает результат возведения числа a в степень b.
    Именованные параметры:
    a -- возводимое число
    b -- степень
    """
    return x ** y


def my_extent_2(a: float, b: int):
    """Возвращает результат возведения числа a в степень b.
    Именованные параметры:
    a -- возводимое число
    b -- степень
    """
    result = a
    for _ in range(abs(b) - 1):
        result *= a
    return 1/result


while True:
    user_input = input(str_question1)
    try:
        x = float(user_input)
        if not x > 0:
            print(str_bad_input)
            continue
        break
    except ValueError as error:
        print(str_bad_input)
        continue

while True:
    user_input = input(str_question2)
    try:
        y = int(user_input)
        if y == abs(y):
            print(str_bad_input)
            continue
        break
    except ValueError as error:
        print(str_bad_input)
        continue

print(f"{str_answer} {my_extent_1(x, y)}")
print(f"{str_answer} {my_extent_2(x, y)}")
