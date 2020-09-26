"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"{self.name} скорость: {self.speed}")


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Превышена допустимая скорость!")


class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Превышена допустимая скорость!")


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


obj_car_1 = TownCar(70, 'Green', 'BMW')
obj_car_2 = SportCar(120, 'Red', 'Ferrari')
obj_car_3 = WorkCar(50, 'Blue', 'Nissan')
obj_car_4 = WorkCar(40, 'Yellow', 'Toyota')
obj_car_5 = PoliceCar(80, 'Black', 'Lada')

print(f"{type(obj_car_1)}: {obj_car_1.name}, {obj_car_1.color}, {obj_car_1.speed}, {obj_car_1.is_police}")
print(f"{type(obj_car_2)}: {obj_car_2.name}, {obj_car_2.color}, {obj_car_2.speed}, {obj_car_2.is_police}")
print(f"{type(obj_car_3)}: {obj_car_3.name}, {obj_car_3.color}, {obj_car_3.speed}, {obj_car_3.is_police}")
print(f"{type(obj_car_4)}: {obj_car_4.name}, {obj_car_4.color}, {obj_car_4.speed}, {obj_car_4.is_police}")
print(f"{type(obj_car_5)}: {obj_car_5.name}, {obj_car_5.color}, {obj_car_5.speed}, {obj_car_5.is_police}")

obj_car_1.go()
obj_car_1.show_speed()
obj_car_1.turn('направо')
obj_car_1.turn('налево')
obj_car_1.stop()

obj_car_2.go()
obj_car_2.show_speed()
obj_car_2.turn('налево')
obj_car_2.turn('направо')
obj_car_2.stop()

obj_car_3.go()
obj_car_3.show_speed()
obj_car_3.turn('налево')
obj_car_3.turn('направо')
obj_car_3.stop()
