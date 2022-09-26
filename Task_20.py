# 20. Даны два файла, в каждом из которых находится запись многочлена.
#     Задача - сформировать файл, содержащий сумму многочленов.

def file_reading(x):
    with open(f'C:/Users/user/OneDrive/Рабочий стол/Edukation IT/Python/DZ/{x}', 'r') as file:
        y = file.read()
    return y

def data_entry_to_file(x):
    with open('file_result.txt', 'a') as file:
        file.writelines(f'{x}\n')

def data_preparetion(x):
    x = str(x)
    x = x.split(' = 0')
    x = x[0].split(' + ')
    for i in range(len(x)):
        x[i] = list(map(int, (x[i].split(sep='x^'))))
    return x

def sum_poli(a, b):
    my_list = []
    if len(a) > len(b):
        k = a
    else:
        k = b
    for i in range(len (k)):
        if len(a[i]) > 1:
            if a[i][1] == b[i][1]:
                my_list.append(a[i][0] + b[i][0])
            elif a[i][1] > b[i][1]:
                my_list.append(a[i][0])
                b.insert(i, a[i][0])
            else: 
                my_list.append(b[i][0])
                a.insert(i, b[i][0])
        else:
            my_list.append(a[i][0] + b[i][0])
    return my_list

num1 = file_reading('textdub20.txt')
num2 = file_reading('text20.txt')
num1 = data_preparetion(num1)
num2 = data_preparetion(num2)
print(num1)
print(num2)
result = sum_poli(num1, num2)
print(result)