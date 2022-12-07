# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
from random import randint

my_list = []
len_list = 30

for i in range(0, len_list):
    my_list.append(randint(0, 10))

print(my_list)

for i in range(0, len(my_list) - 1):
    smallest = i
    for j in range(i + 1, len(my_list)):
        if my_list[j] < my_list[smallest]:
            smallest = j
    my_list[i], my_list[smallest] = my_list[smallest], my_list[i]

print(my_list)
