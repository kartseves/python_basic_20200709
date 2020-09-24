"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from os import path

if __name__ == '__main__':
    in_file_name = "task4_en.txt"
    out_file_name = "task4_ru.txt"
    in_file = ''
    out_file = ''
    my_file_content = ''
    interface_dict = {
        'answer': 'Результат записан в файл:',
        'error_io': 'Возникла ошибка при чтении/записи файла',
        'error_key': 'Не найдена замена для данных в строке №',
    }
    translate_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
    }

    try:
        file_folder = path.dirname(__file__)
        in_file_path = path.join(file_folder, in_file_name)
        out_file_path = path.join(file_folder, out_file_name)

        in_file = open(in_file_path, 'r', encoding='UTF-8')
        out_file = open(out_file_path, 'w', encoding='UTF-8')

        for index, line in enumerate(in_file):
            try:
                line_data = line.split()
                line_data[0] = translate_dict[line_data[0]]
                out_file.write(' '.join(line_data) + '\n')
            except KeyError as error:
                print(f"{interface_dict['error_key']}{index + 1}:")
                print(f"    {line.replace(chr(10),'')}")

        print(f"{interface_dict['answer']} {out_file_path}")

    except IOError as error:
        print(f"{interface_dict['error_io']}: {error}")
    finally:
        if in_file:
            in_file.close()
        if out_file:
            out_file.close()
