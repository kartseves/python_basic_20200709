"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def sum_two_max_out_of_three(one, two, three):
    """Возвращает сумму наибольших двух аргументов из трех.
    Именованные параметры:
    one -- первый аргумент
    two -- второй аргумент
    three -- третий аргумент
    """
    if min(one, two, three) == three:
        result = one + two
    elif min(one, two, three) == two:
        result = one + three
    else:
        result = two + three

    return result


print(sum_two_max_out_of_three(3, 4, 2))
