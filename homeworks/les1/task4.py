"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

str_bad_input = 'Некорректный ввод значения.'
str_question1 = 'Введите целое положительное число:\n'
str_answer = 'Максимальная цифра:'

num_str = input(str_question1)
if num_str.isdigit():
    tmp_int = int(num_str)
    max_digit = 0
    while tmp_int:
        current_digit = tmp_int % 10
        tmp_int = tmp_int // 10
        if max_digit < current_digit:
            max_digit = current_digit
        if max_digit == 9:
            break
    print(f"{str_answer} {max_digit}")
else:
    print(str_bad_input)