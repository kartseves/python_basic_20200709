"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

from os import path

if __name__ == '__main__':
    file_name = "task1.txt"
    my_file = ''
    interface_dict = {
        'question': 'Введите строку для записи в файл (для завершения введите пустую строку):\n',
        'answer': 'Данные записаны в файл:',
        'error': 'Возникла ошибка при записи данных в файл',
    }

    try:
        file_folder = path.dirname(__file__)
        file_path = path.join(file_folder, file_name)

        my_file = open(file_path, 'a', encoding='UTF-8')
        while True:
            user_str = input(interface_dict['question'])
            if user_str:
                my_file.write(user_str + '\n')
            else:
                break
        print(f"{interface_dict['answer']} {file_path}")
    except IOError as error:
        print(f"{interface_dict['error']}: {error}")
    finally:
        if my_file:
            my_file.close()
