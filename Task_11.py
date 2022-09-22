# 11. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
#     стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]
element_odd_position = 0
for i in range(1, len(my_list), 2):
    element_odd_position += my_list[i] 
print(element_odd_position)
