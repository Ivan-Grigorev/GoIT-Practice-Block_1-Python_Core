# # Создать функции действий(+,-,*,/) и функцию calc куда передаем числа и функцию действия.
# # В main сделать ввод 2-х чисел и знака и вызвать функцию calc
#
# def sub(x, y):
#     return x - y
#
#
# def summ(x, y):
#     return x + y
#
#
# def mult(x, y):
#     return x * y
#
#
# def div(x, y):
#     return x / y if y != 0 else "Error"
#
#
# def error(x, y):
#     return "Error"
#
#
# def calc(x, y, func):
#     return func(x, y)
#
#
# dict_op = {
#     "+": summ,
#     "-": sub,
#     "*": mult,
#     "/": div
# }
#
# n1 = int(input(": "))
# n2 = int(input(": "))
# sign = input(": ")
# print(calc(n1, n2, dict_op.get(sign, error)))
#
#############################################

# # написать функцию которая по знаку возращает нужную функцию действия
#
# def sub(x, y):
#     return x - y
#
#
# def summ(x, y):
#     return x + y
#
#
# def mult(x, y):
#     return x * y
#
#
# def div(x, y):
#     return x / y if y != 0 else "Error"
#
#
# def error():
#     return "Error"
#
#
# def calc(sign):
#     return dict_op.get(sign, error)
#
#
# dict_op = {
#     "+": summ,
#     "-": sub,
#     "*": mult,
#     "/": div
# }
#
# n1 = int(input(": "))
# n2 = int(input(": "))
# sign = input(": ")
# func = calc(sign)
# if func != error:
#     print(func(n1, n2))
# else:
#     print(func())
#
########################################
#
# news = []
#
# def add_news():
#     global news
#     title = input("title: ")
#     body = input("body: ")
#     news.append({'title': title, 'body': body})
#
# def read_news():
#     global news
#     print(news)
#
#
# def work():
#     for i in range(3):
#         add_news()
#     read_news()
#
# work()
#
##########################################
#
# from math import pi
# print(pi)
# pi2 = pi + 4
# print(pi)
# print(pi2)
#
##########################################
#
# def adder(val):
#     def inner(x):
#         return x + val
#     return inner
#
#
# two_adder = adder(2)
# #    def two_adder(x):
# #         return x + 2
# print(two_adder(3)) # 5
# print(two_adder(5)) # 7
# print(adder(2)(3))
# #    def three_adder(x):
# #         return x + 3
# three_adder = adder(3)
# print(three_adder(5))   # 8
# print(three_adder(-3))  # 0
#
# print(adder(2)(3))
#
#############################################
#
# def logged_func(func):
#     def inner(x, y):
#         print(f'called with {x}, {y}')
#         result = func(x, y)
#         print(f'result: {result}')
#         return result
#     return inner
#
#
# @logged_func
# def complicated(x, y, ):
#     return x / y
#
# @logged_func
# def summ(x, y):
#     return x + y
#
# print(complicated(2, 3))
# print(summ(2, 3))
#
################################################
#
# # сделать глобальную переменную age. Написать функцию которая делает print("Hello, world!")
# # написать декоратор который заменяет вывод функции, если age < 18
# AGE = 11
#
# def check(func):
#     global AGE
#     if AGE >= 18:
#         func()
#     else:
#         print("Deny")
#
# @check
# def hello_world():
#     print("Hello, World!")
#
# hello_world
#
############################################
