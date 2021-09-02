"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Пользователь вводит две строки. Необходимо их склеить через пробел
и вернуть результат

ПРИМЕРЫ
--------------------------------------------------------------------------------
- ('привет,', 'как дела') -> 'привет, как дела'
- ('Саша', 'Маша') -> 'Саша Маша'
"""


def sum_str(first_str: str, second_str: str) -> str:
    """Склеивает две строки через пробел

    :param first_str: первая строка
    :param second_str: вторая строка

    :return: результат склеивания
    """
    result = f"{first_str} " + second_str
    return result


if __name__ == '__main__':
    f_str = input('Введите первую строку: ')
    s_str = input('Введите вторую строку: ')
    print(f'Склеенная строка: {sum_str(f_str, s_str)}')
