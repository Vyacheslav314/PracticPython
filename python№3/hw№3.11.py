# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

n = input('Введите строку ')

try:
    float(n)
    if n.find('.') != -1 and n.count('.') == 1 and n.find('.') != 0:
        print('да')
    else:
        raise ValueError
except ValueError:
    print('нет')