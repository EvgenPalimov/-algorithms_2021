"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random


def game(attempts=10):
    secret_number = random.randint(0, 100)
    print(f"Вам предоставлено {attempts} попыток, что б угадать загаданное число!")
    user_answer = int(input("Введите ваше число: "))
    if user_answer == secret_number:
        return f"Поздравляю! Вы выиграли, было загадано число - {secret_number}"
    elif attempts == 1:
        return f"У вас закончились попытки, отгадать число.\n" \
               f"Было загадано, вот такое число - {secret_number}"
    elif user_answer == 777:
        return "Спасибо, что были с нами!!!"
    else:
        if secret_number < user_answer:
            print("Ваше число меньше загаданого, повторите попытку!")
            return game(attempts - 1)
        elif secret_number > user_answer:
            print("Ваше число больше загаданого, повторите попытку!")
            return game(attempts - 1)


print("Добро пожаловать, в нашу игру угадайку!!!\n"
      "Ваша задача, угадать загаданое число от 0 до 100 или набирите '777' для окончания игры!")
print(game())
