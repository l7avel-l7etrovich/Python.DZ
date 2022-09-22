# 18. Задайте последовательность чисел. Напишите программу, которая выведет список
#     неповторяющихся элементов исходной последовательности.
#     [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


num = [1, 1, 2, 3, 4, 5, 5]

def get_list(num1):
    result1 = []
    for i in num1:
        if num1.count(i) == 1:
            result1.append(i)
    return(result1)
print(get_list(num))
print(set(num))