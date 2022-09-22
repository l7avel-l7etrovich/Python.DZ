# 16. Вычислить число c заданной точностью d
#     Пример: при $d = 0.001, π = 3.141

from math import pi 

print("Введите заданную точность: ")
d = int(input('d = '))
num = pi
print(f'{round(num, d)}')

