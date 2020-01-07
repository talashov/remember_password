import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
name = input("Введите для чего какого сервиса вам нужен пароль: ")
password = ""
for x in range(8, 23):
    password = password + random.choice(chars)
print("Ваш парооль от " + name + ": " + password)
input("Нажми Enter для выхода")