"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

str_bad_input = 'Некорректный ввод значения.'
str_question1 = 'Введите время в секундах:\n'
str_answer = 'Время в часах, минутах, секундах'

num_sec_str = input(str_question1)
if num_sec_str.isdigit():
    tmp_int = int(num_sec_str)
    var_hh = tmp_int // (60 * 60)
    tmp_int = tmp_int % (60 * 60)
    var_mm = tmp_int // 60
    tmp_int = tmp_int % 60
    print(f"{str_answer}: {var_hh:0>2d}:{var_mm:0>2d}:{tmp_int:0>2d}")
else:
    print(str_bad_input)
