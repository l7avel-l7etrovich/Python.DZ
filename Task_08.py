# 8. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.


k = int(input(''))
sum = 0
counter = 1
while counter <= k:
    sum += (1+1/counter)**counter
    counter += 1
print(sum)
