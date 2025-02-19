"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

# Вариант - 1
# Хранение реализовано, через словарь, где ключ - это логин, а знчение - это список, с паролем
# и меткой (где метка, имеет флаг: 1 - аккаунт активирован, 0 - аккаунт не активирован)

def authentication_1(): # O(n Log(n)) - линейно-логарифмическая

    while True:  # O(n Log(n)) - линейно-логарифмическая
        login = input("Введите пожалуйста логин: ")  # O(1) - константная
        password = input("Введите пожалуйста пароль: ")  # O(1) - константная
        if users.get(login) and users.get(login)[0] == password and users.get(login)[1] == 1:  # O(1) - константная
            print(f"Вы вошли, под логином {login}.")  # O(1) - константная
            break  # O(1) - константная
        elif users.get(login) and users.get(login)[0] == password and users.get(login)[1] == 0:  # O(1) - константная
            print("Ваша учетная запись не актирована, хотели бы выполнить активацию?")  # O(1) - константная
            answer = input("Выбирете да или нет.")  # O(1) - константная
            if answer == "да":  # O(1) - константная
                users.update({login: [password, 1]})  # O(1) - константная
                print(f"Вы успесшно актировали аккаунт. Вы вошли, под логином {login}.")  # O(1) - константная
                break  # O(1) - константная
            elif answer == "нет":  # O(1) - константная
                print("Все доброго!")  # O(1) - константная
                break  # O(1) - константная
        else:  # O(1) - константная
            print("Ваш логин или пароль введен не верно, повторите ввод!")  # O(1) - константная


# Вариант - 2

def authentication_2():  # O(1) - константная
    login = input("Введите пожалуйста логин: ")  # O(1) - константная
    password = input("Введите пожалуйста пароль: ")  # O(1) - константная
    if users.get(login) and users.get(login)[0] == password and users.get(login)[1] == 1:  # O(1) - константная
        print(f"Вы вошли, под логином {login}.")  # O(1) - константная
    elif users.get(login) and users.get(login)[0] == password and users.get(login)[1] == 0:  # O(1) - константная
        print("Ваша учетная запись не актирована, хотели бы выполнить активацию?")  # O(1) - константная
        answer = input("Выбирете да или нет.")  # O(1) - константная
        if answer == "да":  # O(1) - константная
            users.update({login: [password, 1]})  # O(1) - константная
            print(f"Вы успесшно актировали аккаунт. Вы вошли, под логином {login}.")  # O(1) - константная
        elif answer == "нет":  # O(1) - константная
            print("Все доброго!")  # O(1) - константная
    else:  # O(1) - константная
        print("Ваш логин или пароль введен не верно!")  # O(1) - константная


users = {
    'user1': ['pass1', 1],
    'user2': ['pass2', 1],
    'user3': ['pass3', 0]
}

authentication_1()
authentication_2()

"""
Конешно с точки зрения О-большое, то второй вариант, безусловно выиграл, но нам нужно сделать так, что б ползователь
вводил пароль несколько раз, а не перезапускал программу постояно, с этой точки зрения, с циклом вариант выигрывает,
но можно ограничть количество попыток, сделать например 3 со счетчиком.
С точки зрения поставленой задачи, я бы предпочел первый вариант с циклом.
"""