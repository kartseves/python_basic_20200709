"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    date_str = '01-01-0001'
    is_valid = True
    day = 1
    month = 1
    year = 1

    def __init__(self, date_str: str):
        self.date_str = date_str
        is_extracted, day, month, year = MyDate.num_extractor(date_str)
        if is_extracted:
            try:
                self.is_valid, error = MyDate.valid_date(day, month, year)
                if self.is_valid:
                    self.day, self.month, self.year = day, month, year
                else:
                    raise ValueError(error)
            except ValueError as error:
                print(f"Ошибка валидации даты: {error}")
        else:
            self.is_valid = False

    @classmethod
    def num_extractor(cls, date_str: str):
        try:
            date_str_list = date_str.split('-')
            return True, int(date_str_list[0]), int(date_str_list[1]), int(date_str_list[2])
        except IndexError as _:
            print(f"Ошибка извлечения даты: Ожидается формат DD-MM-YYYY")
            return False, 1, 1, 1
        except ValueError as _:
            print(f"Ошибка извлечения даты: Ожидается формат DD-MM-YYYY")
            return False, 1, 1, 1

    @staticmethod
    def valid_date(day: int, month: int, year: int):
        if year < 1:
            return False, 'Значение номера года некорректно!'
        if month < 1 or month > 12:
            return False, 'Значение номера месяца некорректно!'
        if day < 1:
            return False, 'Значение номера числа некорректно!'

        if month != 2:
            is_valid = (day < 32) if (month > 7 and not(month & 1)) or (month < 8 and month & 1) else (day < 31)
        else:
            is_valid = (day < 29) if year % 4 or (not year % 100 and year % 400) else (day < 30)

        return is_valid, '' if is_valid else 'Значение номера числа некорректно!'

    def __str__(self):
        if self.is_valid:
            return f"{self.date_str} - число: {self.day:0>2d}, месяц: {self.month:0>2d} год: {self.year:0>4d}"
        else:
            return f"{self.date_str} - дата некорректна"


if __name__ == '__main__':
    print(MyDate("01-02-2020"))
    print(MyDate("31-05-2020"))
    print(MyDate("07-09-2020"))
    print(MyDate("29-02-2020"))
    print(MyDate("29-02-2000"))
    print('-' * 30)
    print(MyDate("ывапываыва"))
    print(MyDate("05-13-ывав"))
    print(MyDate("05-03-0000"))
    print(MyDate("05-13-2020"))
    print(MyDate("31-02-2020"))
    print(MyDate("31-09-2020"))
    print(MyDate("29-02-1900"))
