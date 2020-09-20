"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета
для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys


def salary(work_time: int, rate: float, prize: float) -> float:
    """Возвращает размер заработной платы сотрудника.
    Именованные параметры:
    work_time -- выработка в часах
    rate -- ставка в час
    prize -- премия
    """
    return (work_time * rate) + prize


if len(sys.argv) > 3:
    _, work_time_str, rate_str, prize_str = sys.argv

    print(f"Заработная плата: {salary(int(work_time_str), float(rate_str), float(prize_str))}")
