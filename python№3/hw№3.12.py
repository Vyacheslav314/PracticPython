# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между
# первой и последней буквой "о" из исходной строки.
# Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.


my_str = input('Введите строку ')
my_str2 = ''

if my_str.count('о') == 0:
    print('Буква "о" не встречается в этой строке ')
elif my_str.count('о') == 1:
    print('Буква "о" встречается в этой строке 1 раз ')
else:
    first_index = 0
    last_index = 0
    for i in range(len(my_str)):
        if my_str[i] == 'о':  # -> рус. расклад.
            first_index = i
            break
    for j in range(len(my_str)-1,first_index, -1):
        if my_str[j] == 'о':
            last_index = j
            break
    for k in range(first_index + 1, last_index):
        my_str2 += my_str[k]
    print(my_str2)
