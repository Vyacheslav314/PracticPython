# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

num = float(input('Введите многозначное число '))
my_list = []
count = 1

while num > 0:
    temp = num % 10
    num = num // 10
    my_list.append(temp)

for i in range(1, len(my_list)):
    if my_list[i - 1] > my_list[i]:
        count += 1

if count == len(my_list):
    print('yes')
else:
    print('no')
