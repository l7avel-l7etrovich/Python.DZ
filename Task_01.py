# 1. Напишите программу, которая принимает на вход цифру, 
#    обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

from ast import List

print('Эта программа, принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')
day = int(input('Введите цифру от 1 до 7, обозначающую день недели: '))
List = [1, 2, 3, 4, 5, 6, 7]

if ((day == 6) or (day == 7)):
    print("Да")
else:
    print("Нет")