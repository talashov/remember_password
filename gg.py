import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
username = input("Введите логин от аккаунта: ")
name = input("Введите для какого сервиса вам нужен пароль: ")
password = ""
for x in range(8, 23):
    password = password + random.choice(chars)
print("\n[ "+ name + " ]" + "\nЛОГИН: " + username + "\nПАРОЛЬ: " + password)
#Создание текстового файла и запись пароля
file = open('pass.txt', 'a')
file.write("\n[ "+ name + " ]" + "\nЛОГИН: " + username + "\nПАРОЛЬ: " + password)
file.close()