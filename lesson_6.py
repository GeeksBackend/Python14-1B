#Исключения try, except
# try:
#     print(100 / 1)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# while True:
#     number1 = int(input("Number1: "))
#     operator = input("+, -, *, /: ")
#     number2 = int(input("Number2: "))
#     if operator == "+":
#         print(number1 + number2)
#     elif operator == "-":
#         print(number1 - number2)
#     elif operator == "*":
#         print(number1 * number2)
#     elif operator == "/":
#         try:
#             print(number1 / number2)
#         except ZeroDivisionError:
#             print("Деление на ноль")
#     elif number1 == 0 and operator == "0" and number2 == 0:
#         print("STOP")
#         break
#     else:
#         print("Operator not found")
    

# name = "Nur"
# try:
#     print(neme)
# except NameError:
#     print("Ошибка на имя переменной")

# try:
#     print(100 / 0)
# except BaseException as error:
#     print("Error:", error)

# raise StopIteration("Специальный вызов ошибки Python StopIteration")

# car = "BMW"
# try:
#     print(car[3])
# except BaseException:
#     raise IndexError("Такой индекс не существует")
# finally:
#     print("Я все равно буду работать")

#string, float, integer, list, tuple, boolean, set, frozenset
# num1 = [10, 20, 30, 40, 50]
# num2 = [30, 40, 50, 60, 70]
# print(num1 + num2)
# print(set(num1 + num2))

# names = {"Nurbolot", "Erbol", "Islam", "Erbol"}
# print(names)
# names.add("Geeks")
# print(names)
# names.add("Erbol")
# print(names)
# names.remove("Islam")
# print(names)
# names.pop()
# print(names)
# names.clear()
# print(names)

# car1 = {"BMW", "LEXUS"}
# car2 = {"LEXUS", "TOYOTA"}
# print(car1.difference(car2))

#Frozenset
# frzn_set = frozenset({10, 10, 20, 20, 30})
# print(frzn_set)

import random

random_number = random.randint(1, 10)
# print(random_number)
attempts = 3
while True:
    attempts -= 1
    # attempts = attempts - 1
    user_number = int(input("Число от 1 до 10: "))
    if random_number == user_number:
        print("Вы выиграли! Поздравляем!")
        break
    elif attempts == 0:
        print("Вы проиграли :( правильный ответ:", random_number)
        break
    else:
        print("Неправильно, у вас", attempts, "попыток")