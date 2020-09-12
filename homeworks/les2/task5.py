"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

ratings_list = [7, 5, 3, 3, 2]
str_bad_input = 'Некорректный ввод значения.'
str_message = 'Рейтинги:'
str_question1 = 'Введите новый элемент рейтинга: '

print(f"{str_message} {ratings_list}")
while True:
    new_rating_str = input(str_question1)
    if new_rating_str.isdigit():
        break
    else:
        print(str_bad_input)

new_rating = int(new_rating_str)

for index, rating_item in enumerate(ratings_list):
    if rating_item < new_rating:
        ratings_list.insert(index, new_rating)
        break
else:
    ratings_list.append(new_rating)

print(f"{str_message} {ratings_list}")
