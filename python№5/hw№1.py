# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = (input('Введите текст '))
text = text.split(' ')
my_text = ''
for i in text:
        res = i.count('а')
        res1 = i.count('б')
        res2 = i.count('в')
        if res == 0 and res1 == 0 and res2 == 0:
            my_text += i+' '
print(my_text)   
