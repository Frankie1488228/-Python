# Задание 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

# def delenie(*args):
#     try:
#         a = int(input('Введите делимое '))
#         b = int(input('Введите делитель '))
#         division = a / b
#
#     except ZeroDivisionError:
#         print('Некорректный делитель (деление на 0 недопустимо)')
#
#     return division
#
#
# print(f' Результат вычисления равен {delenie()}')

# Задание 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

# def anketa(name, surname,year, city, email, telephone):
#
#     return f'Привет, {name}! Пожалуйста, проверь свои анкетные данные: {name}, {surname}, {year}, {city}, {email}, {telephone}'
# print(anketa(name = input('введите имя: '), surname = input('введите фамилию: '), year = int(input('введите год рождения: ')), city = input('введите город проживания: '), email = input('введите @mail: '), telephone = int(input('введите номер телефона: '))))
#

# Задание 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

# def my_func(a, b, c):
#     try:
#         if a >= c:
#             if b >= c:
#                 return a + b
#             elif a > b and a < c:
#                 return a + c
#             else:
#                 return b + c
#         elif a > b and a < c:
#             return a + c
#         else:
#             return b + c
#     except ValueError:
#         return 'You can enter only numbers'
#
# print(f' Сумма наибольших двух аргументов = {my_func(int(input("Введите число №1: ")), int(input("Введите число №2: ")), int(input("Введите число №3: ")))})')

# Задание 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень

# def stepen(x, y):
#     try:
#         x, y = float(x), int(y)
#         first = 1
#         for i in range(abs(y)):
#             first /= x
#         return first
#     except ValueError:
#         return 'Введите число'
#
# первое_число = input('Введите число ')
# второе_число = input('Введите степень числа ')
# print(stepen(первое_число, второе_число))

# Задание 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

# def stroka ():
#     sum_res = 0
#     p = False
#     while p == False:
#         number = input('Input numbers or EX for quit - ').split()
#
#         res = 0
#         for el in range(len(number)):
#             if number[el] == 'ex' or number[el] == 'EX':
#                 p = True
#                 break
#             else:
#                 res = res + 1
#         sum_res = sum_res + res
#         print(f'Current sum is {sum_res}')
#     print(f'Your final sum is {sum_res}')
#
# stroka()

# Задание 6 - 7

# def text (*args):
#     word = input("Введите строку из слов, разделённых пробелом: ")
#     print(word.title())
#     return
#
# text()