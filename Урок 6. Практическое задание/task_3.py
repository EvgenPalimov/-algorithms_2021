"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from decor import decor


@decor
def profilorovka(number):
    def recursive_reverse_mem(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


profilorovka(10)

"""
Время работы функции profilorovka, составило: -0.00001750 сек.
Выполнение функции profilorovka, заняло: 0.0078125 Mib.
Что б можно было профлирововать рекурсию для оценки количества занятого места, надо ее обернуть в функцию.
"""
