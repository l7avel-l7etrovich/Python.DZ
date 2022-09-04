# 5. Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

print('Программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
print('Введите координаты точки А:')
xa = float(input('X: '))
ya = float(input('Y: '))
print('Введите координаты точки B:')
xb = float(input('X: '))
yb = float(input('Y: '))

result = round(sqrt((xa - xb) ** 2 + (ya - yb) ** 2),3)
print(result)
