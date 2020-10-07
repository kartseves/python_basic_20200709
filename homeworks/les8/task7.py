"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class MyComplex:

    def __init__(self, a: float, b: float):
        self.__a = a
        self.__b = b

    def __str__(self):
        return f"({self.a}{'+' if self.b > 0 else '-'}{abs(self.b)}i)"

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: float):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: float):
        self.__b = b

    def __add__(self, other):
        if not isinstance(other, MyComplex):
            raise TypeError(f"Оба слагаемых должны быть экземплярами класса MyComplex!")
        return MyComplex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        if not isinstance(other, MyComplex):
            raise TypeError(f"Оба множителя должны быть экземплярами класса MyComplex!")
        return MyComplex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)


if __name__ == '__main__':
    z1 = MyComplex(-2, 5)
    z2 = MyComplex(3, -7)
    print(f"z1 = {z1}")
    print(f"z2 = {z2}")

    print("-" * 20)
    z3 = z1 + z2
    assert z3.a == 1 and z3.b == -2, 'Плохо сложил'
    print(f"z1 + z2 = {z3}")
    z3 = z1 * z2
    assert z3.a == 29 and z3.b == 29, 'Плохо умножил'
    print(f"z1 * z2 = {z3}")
