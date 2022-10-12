field_line1 = ['_','|','_','|','_']
field_line2 = ['_','|','_','|','_']
field_line3 = ['_','|','_','|','_']

def print_field_line(x):
    for i in x:
        print(i, end='')
        
print_field_line(field_line1)
print()
print_field_line(field_line2)
print()
print_field_line(field_line3)

line_selection = int(input('Введите номер строки '))
column_selection = int(input('Введите номер столбца '))