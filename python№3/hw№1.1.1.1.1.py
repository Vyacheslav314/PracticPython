# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите длину ряда: '))
list_Fibanachi = []
def Fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x > 0:
        return   (Fibonacci(x - 1) + Fibonacci(x - 2))
    if x < 0:
        return (Fibonacci(x + 2) - Fibonacci(x + 1))
    
for i in range(-n,n + 1):
    list_Fibanachi.append(Fibonacci(i))
print(list_Fibanachi)