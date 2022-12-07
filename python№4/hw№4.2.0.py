# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

from random import randint

a = int(input('Введите кол-во строк в массиве '))
b = int(input('Введите кол-во элементов в строке '))
res_list = []

for i in range(0, a):
    my_list = []
    for j in range(0, b):
        my_list.append(randint(0, 10))
    res_list.append(my_list)

for i in range(0, len(res_list)):
    for j in range(0, len(res_list[i])):
        print(res_list[i][j], end=' ')
    print()

res = 0

for i in range(0, len(res_list)):
    for j in range(0, len(res_list[i])):
       res += res_list[i][j]
    res = res / b
    print(f'средне-арифметическое {i + 1} строки = {res} ')
    res = 0
    




