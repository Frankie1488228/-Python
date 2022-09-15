# from sys import argv
# stavka_v_chas, rabochie_chasi, premya = map(int, argv[1:])
#
# print({argv[0]}, {argv[1]}, {argv[2]})
#
# def zarplata(stavka_v_chas, rabochie_chasi, premya):
#     try:
#         dohod = stavka_v_chas * rabochie_chasi + premya
#         print(f'Ваша заработная плата составляет ( в руб.): {dohod}')
#
#     except ValueError:
#         return 'Not a number'
#
#     return dohod
#
# zarplata(stavka_v_chas, rabochie_chasi, premya)


# Задание 2.
# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.

# list_of_numbers = [78,4,0,9,25,87,8,7]
# new_list_of_numbers = [el for i, el in zip(list_of_numbers, list_of_numbers[1:]) if el > i]
# print(f'Итоговый список - {new_list_of_numbers}')

# Задание 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Решите задание в одну строку.

# print(f'Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21: {[el for el in range (20, 240) if el % 20 == 0 or el % 21 == 0]}')

# Задание 4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

# Список_чисел = [7,3,9,7,2,0,3,8,9,2,5,1]
# счёт = [el for el in Список_чисел if Список_чисел.count(el) < 2]
# print(счёт)

# Задание 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка

# from functools import reduce
#
# def spisok(el1, el2):
#          return el1 * el2
#
# print(f' четные числа из выборки: {[el for el in range(99, 1001) if el % 2 == 0]}')
# print(f'результат вычисления произведения всех элементов списка: {reduce,(spisok, [el for el in range(99, 1001) if el % 2 == 0])}')
#

# Задание 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

# from itertools import count
# from typing import List
#
# for el in count(int(input('Введите целое число :'))):
#     print(el)
#     if el > 31:
#         break
#
#
# from itertools import cycle
#
# spisok1 = ['Lyubov','Moscow', True, 25]
# for el in cycle(spisok1):
#     print(el)
#     if el[1]:
#         break

# from itertools import count
# from math import factorial
#
# def fact():
#     for el in count(1):
#         yield factorial(el)
#
# a = fact()
# b = 0
# for i in a:
#     if b < 15:
#         print(i)
#         b += 1
#     else:
#         break