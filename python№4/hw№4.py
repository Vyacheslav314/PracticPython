# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# from random import randint

# max_val=100
# k = int(input('Введите натуральную степень k:'))

# koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val) ]
# poly='+'.join([f'{(j, "")[j == 1]}x^{i}' for i, j in enumerate(koeff) if j][:: -1])

# print(koeff)
# print(poly)

from random import randint
 

k1 = int(input('Введите натуральную степень k:'))
k2 = int(input('Введите вторую натуральную степень числа k для записи второго файла '))

def write_file1(st):
    with open('file№1.txt', 'w') as data:
        data.write(st)

def write_file2(st):
    with open('file№2.txt', 'w') as data:
        data.write(st)

def create_list(x):
    list = []
    for i in range(x + 1):
        list.append(randint(0, 100))    
    return list
    
def writing_polynomial(sp):
    list = sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x=0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] != 0:
                    wr += '+'
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i] != 0:
                    wr += '+'
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]}=0'
    return wr

koef1 = create_list(k1)
koef2 = create_list(k2)
write_file1(writing_polynomial(koef1))
write_file2(writing_polynomial(koef2))