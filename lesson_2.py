# car = "Tesla"
# print(car)
#integer, string, boolean, float
#Строки и методы строк
# str_one = 'Hello Geeks. I\'m Kurmanbek'
# print(str_one)
# str_two = "Hello Geeks. I'm Kurmanbek\nLanguage Python"
# print(str_two)
# str_three = """Hello Geeks. I'm Kurmanbek
# Language Python"""
# print(str_three)
# str_four = '''Hello Geeks. I'm Kurmanbek
# Language Python'''
# print(str_four)

# name = "Nurbolot"
# surname = "Erkinbaev"
# print(name)
# print(surname)
# print("Name:" + name) #Конкатинация - сложение строк (+)
# print("Surname:" + surname)
# print(name + surname)
# number = 3.10
# language = "python"
# print(language + " " + str(number))

# name = input("Name: ")
# print("Welcome, " + name)
# print("How are you? " + name)

# num1 = input("Number One: ")
# num2 = input("Number Two: ")
# print(int(num1) + int(num2))

#Индексы строк
# it = "Geeks"
#      #01234
# print(it)
# print(it[0])
# print(it[3])
# print(it[4])

# #Срезы строк
# language = "Python"
#            #012345
# print(language)
# print(language[0:2])
# print(language[2:5])
# print(language[0:6:3]) #начало, конец, шаг
# name = "Erbol"
# print(name[::-1]) #Переворачивать строку

#Методы строк
# name = "nurBOlOT"
# print(name)
# print(name.title()) #Вызываем Метод title 
# print(name.upper())
# print(name.lower())

input_name = input("Name: ")
print(input_name.title())

text = "Hello World. Hello Geeks And Hello Python"
print(text.count("Hello"))