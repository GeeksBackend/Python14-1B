#Dictionary - Словари
#integer, string, boolean, float, list, tuple, set, frozenset, dictionary
# student = {'name' : 'Alihan', 'age' : 18}
# print(student)
# print(type(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('language', 'Python')
# print(student)
# print(len(student))
# print(student.get('name')) #Получить значение по ключу из словаря
# student.pop('age') #Метод для удаления ключа и значения
# print(student)
# del student['language'] #Еще один способ удаления из словаря
# print(student)
# student['name'] = "Nurbolot" #Способ обновления значения по ключу
# print(student)
# student['address'] = "Amatova 1B" #Если ключа нету то он создаст новый
# print(student)

# car_tesla = {
#     'id' : 103,
#     'brand' : 'Tesla',
#     'model' : 'Model X',
#     'year' : 2023,
#     'color' : 'Black',
# }
# print(car_tesla)
# print(car_tesla['year'])
# print(car_tesla['color'])
# print(car_tesla.get('id'))
# car_tesla['color'] = "White"
# print(car_tesla)
# car_tesla.pop('year')
# print(car_tesla)
# car_tesla.popitem() #Метод удаляет последний элемент из словаря
# print(car_tesla)
# car_tesla.setdefault('odometer', 0)
# print(car_tesla)

# import time 

# contact = [
#     {'name' : 'Nurbolot',
#      'surname' : 'Erkinbaev',
#      'phone' : '0771234567'
#     },
# ]
# print(contact)
# while True:
#     command = input("1 - посмотреть контакты, 2 - добавить, 3 - удалить, 4 - обновить: ")
#     if command == "1":
#         for c in contact:
#             print(c)
#     elif command == "2":
#         add_name = input("Name: ")
#         add_surname = input("Surname: ")
#         add_number = input("Number: ")
#         result = {'name':add_name, 'surname':add_surname, 'phone':add_number, 'created':time.ctime()}
#         contact.append(result)
#         print("Контакт успешно добавлен")
#     elif command == "3":
#         delete_number = input("Delete number: ")
#         for cont in contact:
#             contact.remove(cont)
#             print("Контакт успешно удален")

# language = {"name":"Python", "version":"3.10.8", "date":"08 september 2023"}
# print(language)
# for key, value in language.items():
#     print(key, value)

#Functions - Функции
def hello(): #Создаем функцию python с именем hello
    print("Hello World and Geeks")
# hello()

def add():
    number1 = int(input("Number1: "))
    number2 = int(input("Number2: "))
    print(number1 + number2)
# add()

def mult(number1, number2): 
    print(number1 * number2)
# mult(10, 10)
# mult(3, 9)
# mult(-1, -2)

def welcome(name:str="Geeks") -> str:
    "Эта функция приветствует вас по имени"
    print("Welcome", name)
    print("How are you?", name)
# welcome("Kurmanbek")
welcome()