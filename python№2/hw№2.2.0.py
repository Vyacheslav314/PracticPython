# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

x = int(input('Введите целое число '))
print(f'Вы ввели число {x} ')

first_max_number = 0
second_max_number = 0
count = 0


while x != count:
    print(f'осталось ввести целых чисел {x - count} ')
    num = int(input('Введите целое число '))
    second_max_number = num

    if num > first_max_number:
        second_max_number = first_max_number
        first_max_number = num

    count += 1

print(f'Первое максимальное число {first_max_number}\nвторое максимальное число {second_max_number}')

