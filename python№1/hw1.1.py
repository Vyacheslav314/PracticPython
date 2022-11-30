# # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

    
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not (x or y or z) == (not x and not y and not z))
# Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

salary = int(input('Введите целое число '))
denomination_banknotes = [25, 10, 3, 1]
count = 0

while salary > 0:
    if salary >= denomination_banknotes[0]:
        salary -= denomination_banknotes[0]
        count += 1
    else:
        print(f'Выданно купюр номиналом 25р {count}')
    # if salary >= denomination_banknotes[1]:
    #     count = 0
    #     salary -= denomination_banknotes[1]
    #     count += 1
    # print(f'Выданно купюр номиналом 10р {count}')
    # if salary >= denomination_banknotes[2]:
    #     count = 0
    #     salary -= denomination_banknotes[2]
    #     count += 1
    # print(f'Выданно купюр номиналом 3р {count}')
    # if salary >= denomination_banknotes[3]:
    #     count = 0
    #     salary -= denomination_banknotes[3]
    #     count += 1
    # print(f'Выданно купюр номиналом 1р {count}')
