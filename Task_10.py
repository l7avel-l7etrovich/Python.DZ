# 10. Реализуйте алгоритм перемешивания списка.

import time

b = int(input('Введите длину списка: '))         
def random(x, y):                                 
    time.sleep(0.05)                              
    return int((time.time()% 1) * (y - x)+ x)    

list = []
for j in range(b):
    list.append(random(-b, b))
print(list)

list_index = []
while b != len(list_index):
    a = random(0, b)
    if not(a in list_index): # Проверяте на наличие повторяющихся индексов.
        list_index.append(a)

result_list = []
for k in range(b):
    result_list.append(list[list_index[k]])
print(result_list)








