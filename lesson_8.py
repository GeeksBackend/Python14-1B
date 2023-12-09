"""10) Напишите функцию, которая принимает слово и возвращает True, если слово
изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False."""

# def is_izogramma(word:str='Geeks') -> bool:
#     if len(set(word)) == len(word):
#         print(True)
#     else:
#         print(False)

# is_izogramma("Nur")
# is_izogramma("Hello")

# def frase_words_count(a : str):
#     a = a.lower()
#     lst = a.split()
#     tup = []
#     for i in lst:
#         tup.append(i + " - " + str(lst.count(i)))
#     tup1 = set(tup)
#     print(tup1)
# frase_words_count(input("smth: "))

# def count_word(text:str='Hello hello') -> dict:
#     print(text)
#     lower_text = text.lower().split(",")
#     print(lower_text)
#     space_delete = "".join(lower_text).split()
#     print(space_delete)
#     result = {}
#     for space in space_delete:
#         result.setdefault(space, space_delete.count(space))
#     print(result)
# count_word("Money, money, money, Money it’s always sunny, in the richmen’s world world")

#Модули и работа с файлами
#В Python импортировать модули можно несколькими способами:
#1 - импортировать сам модуль
# import moduls #без окончания .py

# moduls.reverse_word("Bayastan")
# moduls.count_word("Hello")
# print(moduls.it)

#2 - импортировать отдельные определения из модуля
# from moduls import reverse_word, count_word

# reverse_word("Kurmanbek")
# count_word("Django")

#3 - импортировать всё содержимое модуля сразу
# from moduls import *

# reverse_word("Python")
# count_word("API")
# print(it)

# from time import ctime

# print(ctime())

#Работа с файлами. Функция open()
# f = open('test.txt', 'w')
# f.write("Hello World And Geeks IT Courses")
# f.close()

# py = open('open.py', 'w')
# py.write("print('Hello World')")
# py.close()

# read_py = open('lesson_7.py', 'r', encoding='utf-8')
# print(read_py.read())
# read_py.close()

# rus = open('russian.txt', 'w', encoding='utf-8')
# rus.write("Привет всем, как ваши дела? Geeks")
# rus.close()

with open('close.txt', 'w', encoding='utf-8') as close:
    close.write("How are you? Как дела?")

with open('close.txt', 'r', encoding='utf-8') as read_file:
    print(read_file.read())