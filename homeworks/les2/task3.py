"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

str_bad_input = 'Некорректный ввод значения.'
str_question1 = 'Введите номер месяца:\n'
str_answer1 = 'Время года (по списку):'
str_answer2 = 'Время года (по словарю):'

season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {(12, 1, 2): 'Зима', (3, 4, 5): 'Весна', (6, 7, 8): 'Лето', (9, 10, 11): 'Осень'}

while True:
    num_month_str = input(str_question1)
    if num_month_str.isdigit():
        num_month = int(num_month_str)
        if (num_month > 0) and (num_month < 13):
            break
        else:
            print(str_bad_input)
    else:
        print(str_bad_input)

print(f"{str_answer1} {season_list[num_month // 3 if num_month < 12 else 0]}")

for season_key, season_value in season_dict.items():
    if num_month in season_key:
        print(f"{str_answer2} {season_value}")
        break
