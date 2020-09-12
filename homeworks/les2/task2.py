"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

str_bad_input = 'Некорректный ввод значения.'
str_question1 = 'Введите количество элементов списка:\n'
str_question2 = 'Введите элемент списка номер'

while True:
    list_count_str = input(str_question1)
    if list_count_str.isdigit():
        break
    else:
        print(str_bad_input)

list_count = int(list_count_str)
user_list = []
inc = 0
while inc < list_count:
    user_list.append(input(f"{str_question2} {inc + 1}: "))
    inc += 1

print(user_list)

inc = 0
while inc < list_count//2:
    change_item = user_list.pop(2 * inc)
    user_list.insert(2 * inc + 1, change_item)
    inc += 1

print(user_list)
