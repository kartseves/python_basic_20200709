"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

str_bad_input = 'Некорректный ввод значения.'
str_question = 'Введите строку из слов из маленьких латинских букв через пробел): '


def int_func(word: str):
    return word[0].upper() + word[1:]


def is_good_word(word: str):
    result = True
    for word_s in word:
        check_num = ord(word_s)
        if check_num < 97 or check_num > 122:
            result = False
            break
    return result


while True:
    good_input = True
    user_input = input(str_question)
    user_words = user_input.split()
    result_words = []
    for user_word in user_words:
        if is_good_word(user_word):
            result_words.append(int_func(user_word))
        else:
            print(str_bad_input)
            good_input = False
            break
    else:
        break

print(' '.join(result_words))
