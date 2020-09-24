"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

from os import path

if __name__ == '__main__':
    file_name = "task2.txt"
    my_file = ''
    interface_dict = {
        'answer1': 'Количество строк в файле:',
        'answer2': 'Количество слов в строке №',
        'error': 'Возникла ошибка при чтении данных из файла',
    }

    try:
        file_folder = path.dirname(__file__)
        file_path = path.join(file_folder, file_name)

        my_file = open(file_path, 'r', encoding='UTF-8')
        my_file_content = my_file.readlines()
        print(f"{interface_dict['answer1']} {len(my_file_content)}")
        for index, my_file_str in enumerate(my_file_content):
            print(f"{interface_dict['answer2']}{index + 1}: {len(my_file_str.split())}")
    except IOError as error:
        print(f"{interface_dict['error']}: {error}")
    finally:
        if my_file:
            my_file.close()
