# Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

salary = int(input('Введите целое число '))
denomination_banknotes = [25, 10, 3, 1]
my_list = [0, 0, 0, 0]


while salary > 0:
    if salary >= denomination_banknotes[0]:
        salary -= denomination_banknotes[0]
        my_list[0] += 1

    if salary < denomination_banknotes[0] > denomination_banknotes[1]:
        if salary - denomination_banknotes[1] >= 0:
            salary -= denomination_banknotes[1]
            my_list[1] += 1

    if salary < denomination_banknotes[1] > denomination_banknotes[2]:
        if salary - denomination_banknotes[2] >= 0:
            salary -= denomination_banknotes[2]
            my_list[2] += 1

    if salary < denomination_banknotes[2] > denomination_banknotes[3]:
        if salary - denomination_banknotes[3] >= 0:
            salary -= denomination_banknotes[3]
            my_list[3] += 1


for i in range(len(my_list)):
    print(f'Выданно купюр номиналом {denomination_banknotes[i]}р в кол-ве {my_list[i]}шт')