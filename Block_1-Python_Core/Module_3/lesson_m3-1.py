l = []
for i in range(2, 11, 2):
    l.append(i)
print(l)

l = [i for i in range(1, 11) if i % 2 == 0]
print(l)
l2 = [i if not i % 2 else 0 for i in range(1, 11)]
print(l2)
l3 = [0 if i % 2 else 1 for i in range(10)]
print(l3)
l4 = [1 if i % 2 else 0 for i in range(10)]
print(l4)
l5 = [i for i in range(10, 0, -1)]
print(l5)
s = input(': ')
l6 = [i for i in s if i in "ljldlnb.,nsssof"]
print(l6)
l7 = [i for i in s if i not in "ljldlnb.,nsssof"]
print(l7)
l8 = [i for i in s if i not in ["aaaaaaaayyyyuuuuu"]]
print(l8)

l = [0] * 10
l[3:5] = [2, 2]
print(l)
a = [[1, 2], [3, 4], [5, 6]]
print(len(a[0]), len(a[1]), len(a[2]))
for i in a:
    print(len(i), end=" ")

a = [[1, 2], [3, 4], [5, 6]]
ans = []
for i in a:
    ans += [sum(i)]
print(ans)

a = [[1, 2], [3, 4], [5, 6]]
ans = []

for i, val in enumerate(a):
    if 3 in val:
        ans += [i]
    print(ans, end="")

# def invite_to_event(username):
#     return (f"Уважаемый(ая){username}\nимеем честь пригласить вас на уникальное событие -\nпредставление нашего нового продукта для чистки ковров.\nСобытие состоится 13 мая 2023 года по адресу:\nг.Киев, проспект Свободы, 234/12")
#
# print(invite_to_event("Jack"))
#
# base_rate = 40
# price_per_km = 10
# total_trip = 0
#
#
# def trip_price(path):
#     global total_trip
#     total_trip += 1
#     trip_price = float(base_rate + (path * price_per_km))
#     return trip_price
#
#
# trip_price(5)
#

# def discount_price(price, discount):
#     def apply_discount(discount):
#         nonlocal price
#         price = 5
#         apply_discount = price - float(discount)
#         return apply_discount
#
#     apply_discount(1)
#     return price
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# odd_numbers = numbers[::2]
# even_numbers = numbers[1::2]
# three_numbers = numbers[2:10:3]
#
# numbers_copy = numbers[:]
# print(numbers_copy)
#
#
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=".")

# Добавить 5 элементов в список и удалить первый и последний элемент (удаление сделать 2 способами - функциями и slice)
list_a = []
list_b = ('a', 'b', 'c', 'd', 'e')
list_a.extend(list_b)
print(list_a)

list_a = ['a', 'b', 'c', 'd', 'e']
list_a.remove('a')
list_a.remove('e')
print(list_a)

list_a = ['a', 'b', 'c', 'd', 'e']
list_b = list_a[1:-1]
print(list_b)

# создать список чисел от 10 до 20
list_a = [i for i in range(10, 21)]
print(list_a)

# сгенерировать список [1, 1, 1, 2, 2, 2 , 3, 3, 3]
# не получилось сделать...

# сгенерировать список [1, 2, 1, 1, 2, 3 , 1, 2, 3]
# не получилось сделать...

# посчитать сумму чисел в списке
list_a = [i for i in range(10, 21)]
sum = 0

for i in list_a:
    sum += i
print(list_a)
print(sum)

# создать список списков вывести список количества 2 в каждом из списков
# не получилось составить список количества 2 в каждом из списков, а только вывести количество 2
list_a = [[1, 2], [2, 3], [5, 8], [2, 2]]
list_b = []

for i, val in enumerate(list_a):
    if 2 in val:
        i += 1
        list_b = [i]
print(list_a)
print(list_b)

# создать список списков вывести список индексов списков где нет 2
list_a = [[1, 2], [2, 3], [5, 8], [2, 2]]
list_b = []

for i, val in enumerate(list_a):
    if 2 not in val:
        list_b += [i]
print(list_a)
print(list_b)
