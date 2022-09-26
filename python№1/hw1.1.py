# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from tkinter import Y

x = int(input('Введите X '))
y = int(input('Введите Y '))
z = int(input('Введите Z '))

first_expression = not (x or y or z)
second_expression = not x and not y and not z
isValid = first_expression == second_expression

if isValid == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")