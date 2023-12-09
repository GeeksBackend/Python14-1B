#Циклы for, while
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)

# for geeks in range(1001):
#     print(geeks)

# for number in range(1, 101):
#     print("Geeks IT", number)

# for n in range(1, 101, 2):
#     print(n)

# for number in range(2, 201):
#     if number % 2 == 0:
#         print(number, "четный")
#     else:
#         print(number, "нечетный")

# cars = ["BMW", "Tesla", "Zeekr", "BYD", "Lexus"]
# print(cars)
# print(len(cars))
# for car in cars:
#     print(car)

# name = "Nurbolot"
# print(name)
# for n in name:
#     if n == "b":
#         print("b есть")

# numbers = (10, 4, 5, 56, 77, 12, 1, 3, 200, 333, 666)
# for number in numbers:
#     if number % 2 == 0:
#         print(number, "четный")
#     else:
#         print(number, "нечетный")

# import random

# len_password = int(input("Длина пароля: "))
# count_password = int(input("Количество паролей: "))
# letters = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()?"

# for c in range(count_password):
#     result = ""
#     for i in range(len_password):
#         choice = random.choice(letters)
#         # result = result + choice
#         result += choice
#     print(c + 1, result)

# num1 = 10
# num2 = 20
# while num1 < num2:
#     num1 += 1
#     print(num1)

# n = 0
# while True:
#     n += 1
#     print(n)
#     if n == 10000:
#         print("STOP")
#         break

# for num in range(1, 1001):
#     print(num)
#     if num == 500:
#         print("BREAK")
#         break
#     else:
#         print("continue")
#         continue

# import time 

# progress = 0
# while True:
#     time.sleep(0.1)
#     progress += 5
#     print("HACKING", str(progress) + "%")
#     if progress == 100:
#         print("HACKED")
#         break