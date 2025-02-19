"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

ф-ции min() и sort() не исп-ем!
"""


# Первая функция

def min_number_1(lis):  # O(n^2) - квадратичная
    """"
    Функция для нахождения минимального значения в списке
    param:List:
    return
    """

    res = 0

    for num_1 in lis:  #  O(n) - линейная
        for num_2 in lis:  #  O(n) - линейная
            if num_1 < num_2:  #  O(n) - линейная
                res = num_1  # O(1) - константная
    return res  # O(1) - константная


lis_1 = [1, 123, 65, 0, -14, 45, 87, -54]

print(f"Минимальное значение из списка, равняеться: {min_number_1(lis_1)}")

# Вторая функция

def min_number_2(lis):  #  O(n) - линейная
    """"
    Функция для нахождения минимального значения в списке
    param:List:
    return
    """
    # Преположим что это минимальное число
    min_number = lis[0]  #  O(1) - константная

    for i in range(1, len(lis)):  #  O(n) - линейная
        if lis[i] < min_number:  #  O(n) - линейная
            min_number = lis[i]  #  O(1) - константная

    return min_number  #  O(1) - константная


lis_2 = [1, 123, 65, 0, -14, 45, 87, -54, -87]

print(f"Минимальное значение из списка, равняеться: {min_number_2(lis_2)}")
