# -*- coding:utf -8 -*-
#!/usr/bin/python3

import random

##chars = '+ '
number = input('количество паролей?'+ "\n")
length = input('длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
    input('Press ENTER to exit')
