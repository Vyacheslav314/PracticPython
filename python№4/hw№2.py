# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


num = int(input("Введите число: "))
divider = 2 
my_list = []
while divider <= num:
    if num % divider == 0:
        my_list.append(divider)
        num //= divider
    else:
        divider += 1
print(my_list)   