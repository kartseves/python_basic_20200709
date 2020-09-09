"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена
составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить
одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

str_bad_input = 'Некорректный ввод значения.'
str_question1 = 'Введите результат в первый день:\n'
str_question2 = 'Введите конечный результат:\n'
str_answer_header = 'Результат:'
str_answer_body = '-й день: '
str_answer_footer_part1 = 'Ответ: на '
str_answer_footer_part2 = '-й день спортсмен достиг результата — не менее '
str_answer_footer_part3 = ' км.'

inc_percent = 10

first_day_str = input(str_question1)
if first_day_str.isdigit():
    current_result = int(first_day_str)

    target_str = input(str_question2)
    if target_str.isdigit():
        target_result = int(target_str)

        print(f"{str_answer_header}")

        day_num = 1
        while current_result < target_result:
            print(f"{day_num}{str_answer_body}{current_result:.2f}")
            day_num += 1
            current_result += current_result*inc_percent / 100
        else:
            print(f"{day_num}{str_answer_body}{current_result:.2f}")

        print(f"{str_answer_footer_part1}{day_num}{str_answer_footer_part2}{target_str}{str_answer_footer_part3}")
    else:
        print(str_bad_input)
else:
    print(str_bad_input)