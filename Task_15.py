# 15. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

a = int(input('Введите число:'))
b, c = 0, 1
fib = [b, c]
for i in range(a - 1):
    fib.append(b + c)
    b, c = c, b + c
b_n, c_n = 0, 1
fib_n = [b_n, c_n]
for i in range(a - 1):
    fib_n.append(b_n - c_n)
    b_n, c_n = c_n, b_n - c_n
fib_n.reverse()    # переворачивает значения
fib_n.remove(0)     # убирает значение 
fib_result = fib_n + fib

print(fib_result)
