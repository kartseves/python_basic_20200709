"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

str_bad_input = 'Некорректный ввод значения.'
str_question = 'Введите строку чисел через пробел (для завершения введите в строке "q"): '


def user_input():
    continue_flag = 1
    user_str = input(str_question)
    user_list = user_str.split()
    data_list = []
    try:
        for item in user_list:
            data_list.append(float(item))
    except ValueError as error:
        if item.lower() == 'q':
            continue_flag = 0
        else:
            print(str_bad_input)
            continue_flag = 2
    return data_list, continue_flag


accumulator = 0
while True:
    user_input_result = user_input()
    if user_input_result[1] > 1:
        continue
    accumulator += sum(user_input_result[0])
    print(accumulator)
    if user_input_result[1] > 0:
        continue
    break


