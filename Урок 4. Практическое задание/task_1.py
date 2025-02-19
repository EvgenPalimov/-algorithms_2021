"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for j, i in enumerate(nums) if not j % 2]
    return new_arr


def func_3(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(f"Время работы функции {func_1.__name__} составило {timeit('func_1', globals=globals())} сек.")
print(f"Время работы функции {func_2.__name__} составило {timeit('func_2', globals=globals())} сек.")
print(f"Время работы функции {func_3.__name__} составило {timeit('func_3', globals=globals())} сек.")

"""
Инзначательное время работы функции составило 0.15286669999999997 сек. и имела сложность O(n).
Мною были предложены два варианта, через лист компрехенсив, первый через встроенную функцию enumerate и второй через
range.
Получил вот такие замеры:
Время работы функции func_1 составило 0.11560209999999999 сек.
Время работы функции func_2 составило 0.06408739999999999 сек.
Время работы функции func_3 составило 0.06069459999999999 сек.
Из отчетов модуля профилирования timeit, видно что функция - func_2 более эфективна на 80% в соотношении с функцией - 
func_1. А функция - func_3 еще более эфективная, по сравнения с функцией - func_1, время уменшилось на 90%, а по
сравнению с функцией - func_2, разница составила 5%.
Итого: Исходя из данных представленых выше. func_3 время выполнения уменшилось почти в 2 раза, по сравнению с 
функцией func_1.
"""

