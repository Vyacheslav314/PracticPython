from random import randint


field_line1 = ['_', '|', '_', '|', '_']
field_line2 = ['_', '|', '_', '|', '_']
field_line3 = ['_', '|', '_', '|', '_']


def print_field_line(x):
    for i in x:
        print(i, end='')


def print_field():
    print_field_line(field_line1)
    print()
    print_field_line(field_line2)
    print()
    print_field_line(field_line3)
    print()


def select_line(x):
    if x == 1:
        return field_line1
    if x == 2:
        return field_line2
    if x == 3:
        return field_line3


def select_colums(x):
    if x == 1:
        return 0
    if x == 2:
        return 2
    if x == 3:
        return 4


def tern_man():
    print('Ходят х ')
    line_selection = int(
        input('Введите номер строки. номер строки начинается с 1 и заканчивается 3  '))
    column_selection = int(
        input('Введите номер столбца. номер столбца начинается с 1 и заканчивается 3  '))
    if select_line(line_selection)[select_colums(column_selection)] != '0' and select_line(line_selection)[select_colums(column_selection)] != 'x':
        select_line(line_selection)[select_colums(column_selection)] = 'x'
    else:
        print('выбранные координаты не доступны ')
        tern_man()


def ter_bot():
    print('Ходят 0 ')
    line_selection = int(
        input('Введите номер строки. номер строки начинается с 1 и заканчивается 3  '))
    column_selection = int(
        input('Введите номер столбца. номер столбца начинается с 1 и заканчивается 3  '))
    if select_line(line_selection)[select_colums(column_selection)] != '0' and select_line(line_selection)[select_colums(column_selection)] != 'x':
        select_line(line_selection)[select_colums(column_selection)] = '0'
    else:
        print('выбранные координаты не доступны ')
        ter_bot()


print_field()
count = 0
while count <= 0:
    if (
        field_line1[0] == field_line1[2] == field_line1[4] == 'x'
        or field_line2[0] == field_line2[2] == field_line2[4] == 'x'
        or field_line3[0] == field_line3[2] == field_line3[4] == 'x'
        or field_line1[0] == field_line2[0] == field_line3[0] == 'x'
        or field_line1[2] == field_line2[2] == field_line3[2] == 'x'
        or field_line1[4] == field_line2[4] == field_line3[4] == 'x'
        or field_line1[0] == field_line2[2] == field_line3[4] == 'x'
        or field_line1[4] == field_line2[2] == field_line3[0] == 'x'
    ):
        count = 1
        print('Победили х ')
        break
    else:
        tern_man()
        print_field()
    if (
        field_line1[0] == field_line1[2] == field_line1[4] == '0'
        or field_line2[0] == field_line2[2] == field_line2[4] == '0'
        or field_line3[0] == field_line3[2] == field_line3[4] == '0'
        or field_line1[0] == field_line2[0] == field_line3[0] == '0'
        or field_line1[2] == field_line2[2] == field_line3[2] == '0'
        or field_line1[4] == field_line2[4] == field_line3[4] == '0'
        or field_line1[0] == field_line2[2] == field_line3[4] == '0'
        or field_line1[4] == field_line2[2] == field_line3[0] == '0'
        ):
        count = 1
        print('Победили 0 ')
        break
    else:
        ter_bot()
        print_field()
    
    
