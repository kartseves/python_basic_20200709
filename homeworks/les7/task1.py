"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы. Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list_of_lists: list):
        num_column = 0
        for ind, row in enumerate(list_of_lists):
            if type(row) == list:
                if ind > 0:
                    if len(row) != num_column:
                        raise TypeError('Число элементов в строках матрицы должно быть одинаковым!')
                elif row:
                    num_column = len(row)
                else:
                    raise TypeError('Число элементов в строках матрицы должно быть больше 0!')

                for elem in row:
                    try:
                        _ = float(elem)
                    except ValueError as error:
                        raise TypeError('Все элементы в строках матрицы должны быть числами!')
            else:
                raise TypeError('Строки матрицы должны быть заданы списками!')
        self.list_of_lists = list_of_lists
        self.__num_column = num_column
        self.__num_rows = ind + 1

    def __str__(self):
        return '\n'.join([' '.join([f"{elem:4}" for elem in row]) for row in self.list_of_lists])

    def __add__(self, other):
        if self.__num_rows != other.__num_rows or self.__num_column != other.__num_column:
            raise TypeError('Операция может быть выполнена только для матриц с одинаковой размерностью!')
        result_row = []
        for ind_row in range(self.__num_rows):
            result_column = []
            for ind_column in range(self.__num_column):
                result_column.append(self.list_of_lists[ind_row][ind_column] + other.list_of_lists[ind_row][ind_column])
            result_row.append(result_column)
        return Matrix(result_row)


if __name__ == '__main__':
    matrix_a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    matrix_b = Matrix([[12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
    print('Матрица A:')
    print(matrix_a)
    print('Матрица B:')
    print(matrix_b)
    print('Матрица A + Матрица B:')
    print(matrix_a + matrix_b)
