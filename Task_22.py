# 22. Создайте программу для игры с конфетами человек против человека.

#   Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#   Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#   Все конфеты оппонента достаются сделавшему последний ход. 
#   Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота ""интеллектом""

import random
sweets = 100
print('Игра "Забери всё" приветствует тебя!!!')
print('Правила игры: на столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.Все конфеты оппонента достаются сделавшему последний ход.')
type_game = input('Игра против компьютера? y/n: ')
if type_game == 'n':
    user1 = input('Введите имя первого игрока: ').capitalize()
    user2 = input('Введите имя второго игрока: ').capitalize()
    counter = random.randint(0, 1)
    while sweets > 0:
        counter = not counter
        amount_sweets = sweets > 28
        while True:
            try:
                candy = int(input(f'{user1 if counter else user2} ваш ход. На столе осталось {sweets} конфет. Введите кол-в конфет которое вы забераете: '))
                break
            except Exception as errorik:
                print(errorik)
        while candy > (28 if amount_sweets else sweets) or candy <= 0:
            print(f'Введено неверное кол-во конфет введите заново(от 1 до {28 if amount_sweets else sweets})')
            candy = int(input(f'{user1 if counter else user2} ваш ход. На столе осталось {sweets} конфет. Введите кол-в конфет которое вы забераете: '))
        sweets -= candy
    print(f'{user1 if counter else user2} поздравляем вы победили!!!')
else:
    user = input('Введите ваше имя: ').capitalize()
    comp = 'компьютер'
    counter = random.randint(0, 1)
    while sweets > 0:
        candy = 1
        counter = not counter
        amount_sweets = sweets > 28
        if counter == True:
            candy = int(input(f'{user} ваш ход. На столе осталось {sweets} конфет. Введите кол-во конфет которое вы забераете: '))
        else:
            candy = sweets % 29
            if candy == 0:
                candy = random.randint(1, 28)
                print(f'Осталось {sweets} конфет, кажется я проиграл, я возьму {candy} конфет')
                sweets -= candy
                continue
            else:
                print(f'Сейчас мой ход из {sweets} я возьму {candy} конфет')
        while candy > (28 if amount_sweets else sweets) or candy <= 0:
            print(f'Введено неверное кол-во конфет введите заново(от 1 до {28 if amount_sweets else sweets})')
            candy = int(input(f'{user if counter else comp} ваш ход. На столе осталось {sweets} конфет. Введите кол-в конфет которое вы забераете: '))
        sweets -= candy
    print(f'{user if counter else comp} поздравляем вы победили!!!')

