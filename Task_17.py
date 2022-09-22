# 17. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#     "20" -> [2, 2, 5]

num = int(input('Введите число: '))

def is_prime(num: int) -> bool:  # проверка числа на простоту
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_divisors(num: int) -> list:  # поиск простых множителей числа
    prime_fact = []
    for i in range(2, int(num // 2) + 1):  
        if num % i == 0 and is_prime(i):
            prime_fact.append(i)
    return prime_fact

print(f'Уникальные множители {get_prime_divisors(num)}')