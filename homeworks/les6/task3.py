"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    obj_position_1 = Position('Иван', 'Иванов', 'Слеcарь', 15000, 3000)
    obj_position_2 = Position('Петр', 'Петров', 'Директор', 50000, 15000)

    print(obj_position_1.name)
    print(obj_position_1.surname)
    print(obj_position_1.position)
    print(obj_position_1._income)
    print(obj_position_1.get_full_name())
    print(obj_position_1.get_total_income())

    print('-' * 30)

    print(obj_position_2.name)
    print(obj_position_2.surname)
    print(obj_position_2.position)
    print(obj_position_2._income)
    print(obj_position_2.get_full_name())
    print(obj_position_2.get_total_income())
