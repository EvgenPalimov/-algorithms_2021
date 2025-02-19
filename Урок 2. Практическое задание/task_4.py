"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_elements(n, first_value=1.0):
    return first_value if n == 1 else first_value + sum_elements(n - 1, first_value / -2)


if __name__ == "__main__":
    while True:
        try:
            user_answer = int(input("Введите количество элементов или для выхода наберите - 1111: "))
            if user_answer < 1:
                raise ValueError
            elif user_answer == 1111:
                break
            print(sum_elements(user_answer))
        except ValueError:
            print("Вы вели некоректную сумму элементов, введите больше 1!")

    print("Спасибо, что воспользовались моей программой!")
