"""
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

str_bad_input = 'Некорректный ввод значения.'
str_question1 = 'Введите количество товаров: '

str_message = 'Товар №'
str_answer = 'Структура товаров:'

str_pr_question1 = 'Введите название товара: '
str_pr_question2 = 'Введите цену: '
str_pr_question3 = 'Введите количество: '
str_pr_question4 = 'Введите ед. измерения: '

product_template = {
    'title': str_pr_question1,
    'price': str_pr_question2,
    'count': str_pr_question3,
    'msr_unit': str_pr_question4
}

while True:
    list_count_str = input(str_question1)
    if list_count_str.isdigit():
        break
    else:
        print(str_bad_input)

list_count = int(list_count_str)
products = []
for index in range(1, list_count + 1):
    print(f"{str_message} {index}:")
    product_dict = {}
    for key, question in product_template.items():
        product_dict[key] = input(f"    {question}")
    products.append((index, product_dict))

print(f"{str_answer}\n{products}")
