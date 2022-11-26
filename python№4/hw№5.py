# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import re
import itertools


def read_file1():
    with open('file№1.txt', 'r') as data:
       poly = data.read()
       return poly
   
def read_file2():
    with open('file№2.txt', 'r') as data:
       poly1 = data.read()
       return poly1
   
poly1 = read_file1()
poly2 = read_file2()
poly3 = []
poly1 = poly1.replace('=0', '').split('+')
poly2 = poly2.replace('=0', '').split('+')
print(poly1)
def convert_poly(poly):
    poly = [[x for x in list] for list in poly]
    return poly
print(convert_poly(poly1))
if len(poly1) < len(poly2):
    poly1, poly2 = poly2, poly1

dif_len = len(poly1) - len(poly2)
index = dif_len
my_str = ''
my_str1 = ''
my_str2 = ''
for i in range(dif_len, len(poly1)-1):
    while (index - dif_len) < dif_len:
        poly3.append(poly1[index - dif_len])
        index += 1
        print(poly3)
    
    for j in range(len(poly1[i])):
        if poly1[i][j] != 'x':
            my_str += poly1[i][j]
            print(my_str)
        if poly2[i - dif_len][j] != 'x' :
            my_str1 += poly2[i - dif_len][j]
            print(my_str1)
        else:
            while j < len(poly1[i]):
                my_str2 += poly1[i][j]
                j += 1   
            break
    res = int(my_str) + int(my_str1)
    
    poly3.append(str(res) + str(my_str2))
    my_str2 = ''
    my_str1 = ''
    my_str = ''
    if i == len(poly1)-2:
        poly3.append(int(poly1[len(poly1)-1]) + int(poly2[len(poly2)-1]))

sum_poly = ''
for i in poly3:
    if i != poly3[len(poly3)-1]:
        sum_poly += i + '+'  
    else:
        sum_poly += str(i) + '=0'  
print(sum_poly)
      
def write_file(poly):
    with open('file№3.txt', 'w') as data:
        poly = data.write(poly)

    
write_file(sum_poly)