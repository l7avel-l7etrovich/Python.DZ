# 19. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#     (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     Пример:

#     k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

num = int(input('Введите число:'))
num1 = []
for i in range(num, -1, -1):
    num1.append(f'{random.randint(0, 9)}x^{i}')
print(num1)
for i in range(len(num1)):
    if '1x' in num1[i]:
        num1[i] = num1[i].replace('1x', 'x')
    if '0x' in num1[i]:
        num1[i] = num1[i].replace('0x', '')
    if 'x^1' in num1[i]:
        num1[i] = num1[i].replace('x^1', 'x')
    if 'x^0' in num1[i]:
        num1[i] = num1[i].replace('x^0', '')
    
   
print(num1)
result = f"{' + '.join(num1)} = 0"
print(result)

# startwitx('1x') заменить на Х
# startwitx('0x') удалить элемент Х