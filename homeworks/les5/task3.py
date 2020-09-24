"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

from os import path
from statistics import fmean

if __name__ == '__main__':
    file_name = "task3.txt"
    my_file = ''
    my_file_content = ''
    check_salary = 20000
    interface_dict = {
        'answer1': 'Сотрудники, с окладом менее',
        'answer2': 'Средняя величина дохода сотрудников',
        'answer3': 'Файл не содержит корректых данных для расчета.',
        'error_io': 'Возникла ошибка при чтении данных из файла',
        'error_val1': 'Недостаточно данных в строке №',
        'error_val2': 'Возникла ошибка при получении оклада из строки №',
    }

    try:
        file_folder = path.dirname(__file__)
        file_path = path.join(file_folder, file_name)

        my_file = open(file_path, 'r', encoding='UTF-8')
        my_file_content = my_file.readlines()
    except IOError as error:
        print(f"{interface_dict['error_io']}: {error}")
    finally:
        if my_file:
            my_file.close()

    if my_file_content:
        acc_salary = []
        print(f"{interface_dict['answer1']} {check_salary}:")
        for index, my_file_str in enumerate(my_file_content):
            worker_data = my_file_str.split()
            try:
                salary = float(worker_data[1])
                acc_salary.append(salary)
                if salary < check_salary:
                    print(f"    {worker_data[0]} - {salary}")
            except IndexError as error:
                print(f"{interface_dict['error_val1']}{index + 1}:")
                print(f"    {my_file_str.replace(chr(10),'')}")
            except ValueError as error:
                print(f"{interface_dict['error_val2']}{index + 1}:")
                print(f"    {my_file_str.replace(chr(10),'')}")

        print(f"{interface_dict['answer2']}: {fmean(acc_salary) if acc_salary else interface_dict['answer3']}")
