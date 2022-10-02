# Реализуйте алгоритм перемешивания списка.

from random import randint

my_list = [1, 3, 44, 55, 21, 5]


for i in range(len(my_list)):
    r = randint(0,i)
    temp = my_list[r]
    my_list[r] = my_list[i]
    my_list[i] = temp


print(my_list)

