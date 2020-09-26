"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки маркером.')


if __name__ == '__main__':
    obj_stationery = Stationery('Канц. принадлежность 1')
    obj_stationery.draw()

    obj_pen = Pen('Ручка 1')
    obj_pen.draw()

    obj_pencil = Pencil('Карандаш 1')
    obj_pencil.draw()

    obj_handle = Handle('Маркер 1')
    obj_handle.draw()
