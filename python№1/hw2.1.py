# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import math
a = int(input('Укажите номер четверти координат '))

if a == 1:
    print(f'x от 0 до {math.inf} y от 0 до {math.inf}')
elif a == 2:
    print(f'x от 0 до {-math.inf} y от 0 до {math.inf}')
elif a == 3:
    print(f'x от 0 до {-math.inf} y от 0 до {-math.inf}')
elif a == 4:
    print(f'x от 0 до {math.inf} y от 0 до {-math.inf}')