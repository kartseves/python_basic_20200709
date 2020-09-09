"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

item_number = 3
str_bad_input = 'Некорректный ввод значения.'
str_question1 = 'Введите число n (от 1 до 9):\n'
str_answer = 'Сумма чисел'

num_str = input(str_question1)
if num_str.isdigit():
    num_int = int(num_str)

    if num_int < 10:
        item_str = num_str
        item_int = num_int

        exp_str = item_str
        exp_int = item_int

        current_mult = 10
        while current_mult < 10**item_number:
            item_str += num_str
            exp_str += ' + ' + item_str

            item_int += num_int * current_mult
            exp_int += item_int

            current_mult = current_mult * 10

        print(f"{str_answer} {exp_str} = {exp_int}")
    else:
        print(str_bad_input)
else:
    print(str_bad_input)