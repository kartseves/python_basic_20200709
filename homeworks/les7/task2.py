"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_usage(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_usage(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_usage(self):
        return 2 * self.height + 0.3


if __name__ == '__main__':
    coat_1 = Coat('Пальто мужское, бренд 1', 52)
    coat_2 = Coat('Пальто женское, бренд 2', 46)

    suit_1 = Coat('Смокинг, бренд 1', 54)
    
    print(f"{coat_1.name}, расход ткани - {coat_1.fabric_usage}")
    print(f"{coat_2.name}, расход ткани - {coat_2.fabric_usage}")
    print(f"{suit_1.name}, расход ткани - {suit_1.fabric_usage}")
