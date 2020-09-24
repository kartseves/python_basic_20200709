"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

from os import path
from json import dumps, dump

if __name__ == '__main__':
    in_file_name = "task7.txt"
    out_file_name = "task7.json"
    in_file = ''
    out_file = ''
    my_file_content = ''
    interface_dict = {
        'answer1': 'По данным файла сформирован словарь:',
        'answer2': 'Результат преобразования словаря в json:',
        'answer3': 'Результат записан в файл:',
        'error_io': 'Возникла ошибка при чтении/записи файла',
        'error_val1': 'Недостаточно данных в строке №',
        'error_val2': 'Не удалось преобразовать данные в строке №',
        'error_val3': 'Данные фирмы "%1" дублируются в строке №',
    }
    result_dict = dict()

    file_folder = path.dirname(__file__)
    in_file_path = path.join(file_folder, in_file_name)
    out_file_path = path.join(file_folder, out_file_name)

    try:
        profit_count = 0
        profit_result = 0
        with open(in_file_path, 'r', encoding='UTF-8') as in_file:
            for index, line_str in enumerate(in_file):
                line_list = line_str.split()
                try:
                    if result_dict.get(line_list[0]) is None:
                        current_result = float(line_list[2]) - float(line_list[3])
                        result_dict[line_list[0]] = current_result
                        if current_result > 0:
                            profit_count += 1
                            profit_result += current_result
                    else:
                        print(f"{interface_dict['error_val3'].replace('%1', line_list[0])}{index + 1}")
                except IndexError as error:
                    print(f"{interface_dict['error_val1']}{index + 1}:")
                    print(f"    {line_str.replace(chr(10),'')}")
                except ValueError as error:
                    print(f"{interface_dict['error_val2']}{index + 1}:")
                    print(f"    {line_str.replace(chr(10),'')}")

        answer_list = [result_dict, {"average_profit": profit_result/profit_count if profit_count > 0 else None}]
        print(interface_dict['answer1'])
        print(answer_list)

        j_data = dumps(answer_list, ensure_ascii=False)
        with open(out_file_path, 'w', encoding='UTF-8') as out_file:
            dump(answer_list, out_file, ensure_ascii=False)
        print(interface_dict['answer2'])
        print(j_data)
        print(f"{interface_dict['answer3']} {out_file_path}")

    except IOError as error:
        print(f"{interface_dict['error_io']}: {error}")
