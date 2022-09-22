# 14. Напишите программу,
#     которая будет преобразовывать десятичное число в двоичное (без встроенных функций).

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите десятичное число: '))
num1 = num
value = 0
result1 = 0

while num1 > 0:
    value *= 10
    num2 = num1 % 2
    value += num2
    num1 //= 2
while value > 0:
    result1 *= 10
    num2 = value % 10 
    result1 += num2
    value //= 10

print(f'{num} -> {result1}')
   

