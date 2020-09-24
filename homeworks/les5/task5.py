"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from os import path
from random import random

if __name__ == '__main__':
    file_name = "task5.txt"
    my_file = ''
    my_file_content = ''
    num_count = 10
    interface_dict = {
        'answer1': 'Набор случайных чисел записан в файл:',
        'answer2': 'Из файла прочитана строка:',
        'answer3': 'Сумма чисел в строке:',
        'error_io': 'Возникла ошибка при чтении/записи файла',
    }

    try:
        file_folder = path.dirname(__file__)
        file_path = path.join(file_folder, file_name)

        my_file = open(file_path, 'w', encoding='UTF-8')
        for ind in range(0, num_count):
            my_file.write(f"{' ' if ind else ''}{random()*1000:.3f}")
        print(f"{interface_dict['answer1']} {file_path}")
    except IOError as error:
        print(f"{interface_dict['error_io']}: {error}")
    finally:
        if my_file:
            my_file.close()

    try:
        my_file = open(file_path, 'r', encoding='UTF-8')
        my_file_content = my_file.readline()
        print(f"{interface_dict['answer2']} {my_file_content}")
        print(f"{interface_dict['answer3']} {sum(map(lambda x: float(x), my_file_content.split()))}")
    except IOError as error:
        print(f"{interface_dict['error_io']}: {error}")
    finally:
        if my_file:
            my_file.close()
