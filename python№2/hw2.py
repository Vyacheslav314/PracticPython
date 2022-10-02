# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


path = 'file.txt'
data = open(path, 'r')
n = int(input('Введите число '))
my_list = []
res = 0
for i in range(-n, n + 1):
    my_list.append(i)
for line in data:
    res += my_list[int(line)]       
print(my_list)
print(res)
data.close()