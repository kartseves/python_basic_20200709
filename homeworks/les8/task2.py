"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):

    def __init__(self, text):
        self.text = text


def user_input(question: str):
    while True:
        try:
            return float(input(question))
        except ValueError as _:
            print(f"Некорректный ввод!")
            continue


if __name__ == '__main__':
    print("Попробуем вычислить частное.")
    num_up = user_input("Введите числитель:\n")
    while True:
        try:
            num_down = user_input("Введите знаменатель:\n")
            if num_down != 0:
                print(f"Результат: {num_up / num_down}")
                break
            else:
                raise MyZeroDivisionError("На ноль поделить не выйдет!")
        except MyZeroDivisionError as error:
            print(error)
