# 6. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример: - 0,56 -> 11

a = float(input('Введите вещественное число: '))
while (a > 1):
    a /= 10
a = str(a).split(sep='.')
a = int(a[1])
summa = 0
while (a != 0):
    summa += a % 10
    a //= 10


print(f'{a} -> {summa}')
