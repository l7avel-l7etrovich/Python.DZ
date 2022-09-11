# 9. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

import random


n = int(input('Задайте список из N элементов: '))
n_list = []

for i in range(n):
    n_list.append(random.randint(-n, n))
print(n_list)

user_list = input('Введите идекс числа, через пробел, для перемножения: ').split(sep=' ')
user_list = [int(x) for x in user_list]
print(user_list)

mult = 1
for i in range(len(user_list)):
    mult *= n_list[user_list[i]]
print(mult)