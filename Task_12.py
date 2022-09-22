# 12. Напишите программу, которая найдёт произведение пар чисел списка. 
#     Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15];

from math import ceil 

my_list = [2, 3, 4, 5, 6]
result_list = []
for i in range(ceil(len(my_list)/2)):
    result_list.append(my_list[i] * my_list[-i-1])

print(result_list)
