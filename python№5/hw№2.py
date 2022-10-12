# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint


candies = 2022
players = ['человек', 'соперник', 'бот', 'Умный бот']
count_players = [0, 0, 0, 0]

tern = randint(0, 4)

while candies > 0:
    if tern == 0:
        print(f'осталось {candies} конфет ')
        print(f'{players[tern]} ходит у вас {count_players[tern]} конфет ')
        take = int(input('возьмите от 1 до 28 конфет: '))
        if take <= 28 and take > 1:
            count_players[tern] += take
            candies -= take
            print(f'{players[tern]} берёт {take} конфет теперь у него {count_players[tern]}\n')
            take = 0
        else:
            take = int(input('возьмите от 1 до 28 конфет: \n'))
        if candies == 0:
            print(f'{players[tern]} победил!!! ')
    if tern == 1:
        print(f'осталось {candies} конфет ')
        print(f'{players[tern]} ходит у вас {count_players[tern]} конфет')
        take = int(input('возьмите от 1 до 28 конфет: '))
        if take <= 28 and take > 1:
            count_players[tern] += take
            candies -= take
            print(f'{players[tern]} берёт {take} конфет теперь у него {count_players[tern]}\n')
            take = 0
        else:
            take = int(input('возьмите от 1 до 28 конфет: '))
        if candies == 0:
            print(f'{players[tern]} победил!!! ')
    if tern == 2:
        print(f'осталось {candies} конфет ')
        print(f'{players[tern]} ходит у вас {count_players[tern]} конфет')
        take = randint(1,29)
        count_players[tern] += take
        candies -= take
        print(f'{players[tern]} берёт {take} конфет теперь у него {count_players[tern]}\n')
        take = 0
        if candies == 0:
            print(f'{players[tern]} победил!!! ')
    if tern == 3:
        print(f'осталось {candies} конфет ')
        print(f'{players[tern]} ходит у вас {count_players[tern]} конфет ')
        if candies >= 200:
            take = randint(20,29)
            count_players[tern] += take
        if candies <= 112:
            take = randint(10,15)
            count_players[tern] += take
        if candies <= 28:
            take = candies
            count_players[tern] += take
        candies -= take
        print(f'{players[tern]} берёт {take} конфет теперь у него {count_players[tern]}\n')
        take = 0
        if candies == 0:
            print(f'{players[tern]} победил!!! ')
            
        
    tern += 1
    if tern >= 4:
        tern = 0

        
    