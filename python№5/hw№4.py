# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


def read_file():
    with open('file№4.txt', 'r') as data:
       x = data.read()
       return x
   
def write_file(x):
    with open('file№4.txt', 'w') as data:
        x = data.write(x)
   

def compression(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decompression(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if  txt[i].isdigit():
            number = txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

my_string1 = input("Введите текст: ")
my_string2 = read_file()
write_file(compression(my_string1))
print(decompression(my_string2))

