"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Таракан - одно из самых быстрых насекомых.
Нужно отредактировать функцию cockroach_speed, которая принимает скорость
таракана в км/ч так, чтобы она возвращала скорость таракана в см/с
(float округляем вниз)

ПРИМЕРЫ
--------------------------------------------------------------------------------
cockroach_speed(1.08) -> 30
cockroach_speed(2.13) -> 59
"""
from math import floor

def cockroach_speed(kmh_speed: float) -> int:
    """Переводит скорость таракана из км/ч в см/с

    :param kmh_speed: скорость в км/ч

    :return: скорость в см/с
    """
    result = floor(float(kmh_speed) * 27.7777777777778)
    return result


if __name__ == '__main__':
    speed_val = float(input('Введите скорость таракана в км/ч: '))
    print(f'Скорость таракана в см/с: {cockroach_speed(speed_val)}')
