"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы
в расчете на одного сотрудника.
"""

str_bad_input = 'Некорректный ввод значения.'
str_question1 = 'Введите значение выручки:\n'
str_question2 = 'Введите значение издержек:\n'
str_question3 = 'Введите численность сотрудников:\n'

str_profit = 'Фирма отработала с прибылью.'
str_loss = 'Фирма отработала с убытком.'
str_profitability = 'Рентабельность выручки:'
str_profit_by_emp = 'Прибыль фирмы в расчете на одного сотрудника:'

revenue_str = input(str_question1)
if revenue_str.isdigit():
    revenue_int = int(revenue_str)

    cost_str = input(str_question2)
    if cost_str.isdigit():
       cost_int = int(cost_str)

       if revenue_int > cost_int:
           print(f"{str_profit} {str_profitability} {100 * (revenue_int - cost_int)/revenue_int:.2f}%")

           emp_count_str = input(str_question3)
           if emp_count_str.isdigit():
               emp_count_int = int(emp_count_str)
               print(f"{str_profit_by_emp} {(revenue_int - cost_int) / emp_count_int}")
           else:
               print(str_bad_input)
       else:
           print(str_loss)
    else:
        print(str_bad_input)
else:
    print(str_bad_input)

