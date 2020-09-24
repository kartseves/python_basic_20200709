"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и
общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from os import path

if __name__ == '__main__':
    file_name = "task6.txt"
    my_file = ''
    interface_dict = {
        'answer1': 'Количество строк в файле:',
        'answer2': 'Сформирован словарь:',
        'error': 'Возникла ошибка при чтении данных из файла',
        'error_val1': 'Не удалось получить название предмета в строке №',
        'error_val2': 'Данные предмета "%1" дублируются в строке №',
    }
    result_dict = dict()

    try:
        file_folder = path.dirname(__file__)
        file_path = path.join(file_folder, file_name)

        my_file = open(file_path, 'r', encoding='UTF-8')
        my_file_content = my_file.readlines()

    except IOError as error:
        print(f"{interface_dict['error']}: {error}")
    finally:
        if my_file:
            my_file.close()

    print(f"{interface_dict['answer1']} {len(my_file_content)}")
    for index, my_file_str in enumerate(my_file_content):
        try:
            start_index = my_file_str.index(':')
            obj_name = my_file_str[:start_index]
        except ValueError as error:
            print(f"{interface_dict['error_val1']}{index + 1}")
            continue

        if result_dict.get(obj_name) is None:
            obj_data = my_file_str[start_index + 2:].replace(chr(10),'')
            total_value = 0
            current_str = ''
            for symbol in obj_data:
                try:
                    current_str += symbol
                    inc_value = float(current_str)
                except ValueError as error:
                    total_value += inc_value
                    inc_value = 0
                    current_str = ''
            result_dict[obj_name] = total_value
        else:
            print(f"{interface_dict['error_val2'].replace('%1', obj_name)}{index + 1}")

    print(f"{interface_dict['answer2']}\n{result_dict}")
