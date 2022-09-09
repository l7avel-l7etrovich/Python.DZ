# 7. Напишите программу, которая принимает на вход число
#    N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4).

n = int(input('Введите число N: '))
count = 1
fractal = 1
while (count <= n):
    fractal = fractal * count
    count += 1
    if count == 2:
        print(f"[ {fractal}", end=", ")
    elif count == n + 1:
        print(f"{fractal}", end=" ]")
    else:
        print(f"{fractal}", end=", ")





