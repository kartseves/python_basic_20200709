"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

str_question1 = 'Введите текст:\n'

user_str = input(str_question1)
words_list = user_str.split()
for index, word in enumerate(words_list, 1):
    print(f"{index}: {word[:10]}")
