# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

my_list = [1.1, 1.2, 3.1, 5, 10.01]
max_value = my_list[0] - round(my_list[0])
min_value = my_list[0] - round(my_list[0])
for i in range(len(my_list)):
    temp = my_list[i] - round(my_list[i])
    if max_value <= temp:
        max_value = temp

for i in range(len(my_list)):
    temp = my_list[i] - round(my_list[i])
    if min_value >= temp and temp != 0:
        min_value = temp   
res = max_value - min_value

print(round(res, 3))
    
