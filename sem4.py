# Задача 1. Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi
# d = int(input('Введите число: '))
# print(round(pi, d))


# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите число: '))
# a = 2
# list = []
# num = n

# while a <= n:
#     if n % a == 0:
#         list.append(a)
#         n //= a
#     else:
#         a += 1
# print(f'простые множители числа {num}: {list}')


# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint
# num = int(input('Введите количество чисел: '))
# list1 = []
# list2 = []
# for i in range(num):
#     list1.append(randint(1,11))
# print(list1)
# for i in list1:
#     count = 0
#     for j in list1:
#         if i == j:
#             count += 1
#     if count == 1:
#         list2.append(i)
# print(list2)

# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# from random import randint
# k = int(input('Введите натуральную степень k: '))

# def create_file(fl):
#     with open ('text.txt', 'a') as data:
#         data.write(fl)
# def create_list(k):
#     list = []
#     for i in range(k + 1):
#         list.append(randint(0, 101))    
#     return list
# def create_string(st):
#     list = st[::-1]
#     a = ''
#     if len(list) < 1:
#         a = 'x = 0'
#     else:
#         for i in range(len(list)):
#             if i != len(list) - 1 and i != len(list) - 2 and list[i] != 0:
#                 a += f'{list[i]}x**{(len(list)) - i - 1}'
#                 if list[i + 1] != 0:
#                     a += ' + '
#             elif i == len(list) - 2 and list[i] != 0:
#                 a += f'{list[i]}x'
#                 if list[i + 1] != 0:
#                     a += ' + '
#             elif i == len(list) - 1 and list[i] != 0:
#                 a += f'{list[i]} = 0'
#             elif i == len(list) - 1 and list[i] == 0:
#                 a += ' = 0'
#     return a
# kf = create_list(k)
# create_file(create_string(kf) + '\n')





# задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


