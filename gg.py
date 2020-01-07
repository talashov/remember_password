import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
<<<<<<< HEAD
username = input("Введите логин от аккаунта: ")
=======
>>>>>>> 44e6af2333877f8f0ec17997832711a925b6923f
name = input("Введите для какого сервиса вам нужен пароль: ")
password = ""
for x in range(8, 23):
    password = password + random.choice(chars)
print("\n[ "+ name + " ]" + "\nЛОГИН: " + username + "\nПАРОЛЬ: " + password)
#Создание текстового файла и запись пароля
file = open('pass.txt', 'a')
<<<<<<< HEAD
file.write("\n[ "+ name + " ]" + "\nЛОГИН: " + username + "\nПАРОЛЬ: " + password)
file.close()
=======
file.write("\nВаш парооль от " + name + ": " + password)
file.close()
>>>>>>> 44e6af2333877f8f0ec17997832711a925b6923f
