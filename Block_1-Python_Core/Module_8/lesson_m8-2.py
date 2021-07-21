# import random
#
# d = {
#     "q1?": [["a", "b", "c", "d"], "a"],
#     "q2?": [["a", "b", "c", "d"], "b"],
#     "q3?": [["a", "b", "c", "d"], "c"],
#     "q4?": [["a", "b", "c", "d"], "d"],
# }
# lq = random.sample(list(d.keys()), 3)
# for i in lq:
#     random.shuffle(d[i][0])
#     print(f"{i} answers:\n{d[i][0]}")
#

#
# from datetime import datetime
#
#
# def get_days_from_today(date):
#     date1 = date.split("-")
#     current_date = datetime.now()
#     date2 = datetime(year=int(date1[0]), month=int(date1[1]), day=int(date1[2]))
#     difference = current_date - date2
#     print(difference.days)
#     return difference.days
#
#
# get_days_from_today("2021-10-09")

#
# from datetime import date
# import calendar
#
#
# def get_days_in_month(month, year):
#     days = calendar.monthrange(year, month)
#     print(days[1])
#     return days[1]
#
#
# get_days_in_month(3, 2021)
#
#

# from datetime import datetime
#
#
# def get_str_date(date):
#     date1 = date.replace("-", " ")
#     date2 = date1.split()
#     date3 = datetime(year=int(date2[0]), month=int(date2[1]), day=int(date2[2]))
#     return date3.strftime('%A %d %B %Y')
#
#
# print(get_str_date("2021-05-27 17:08:34.149Z"))


#
# from random import randrange
#
#
# def get_numbers_ticket(min, max, quantity):
#     new_num1 = []
#     if min < 1 or max > 1000 or quantity < min or quantity > max:
#         return []
#     for i in range(quantity):
#         new_num = randrange(min, max)
#         if new_num not in new_num1:
#             new_num1.append(new_num)
#         i += 1
#     new_num1.sort()
#     return new_num1
#
#
# print(get_numbers_ticket(1, 49, 6))
#
#
# import random
#
#
# def get_random_winners(quantity, participants):
#     new_list = []
#     new_list1 = []
#     if len(participants) < quantity:
#         return []
#     for key in participants.keys():
#         new_list.append(key)
#         random.shuffle(new_list)
#     new_list1 = random.sample(new_list, k=quantity)
#     return new_list1
#
#
# print(get_random_winners(2, {'605884760742316c07eae603': 'vitanlhouse@gmail.com',
#                              '605b89080c318d66862db390': 'elhe2013@gmail.com',
#                              "603d2cec9993c627f0982404": "test@test.com",
#                              "603f79022922882d30dd7bb6": "test11@test.com",
#                              "60577ce4b536f8259cc225d2": "test2@test.com",
#                              }))
#
#
#
# from decimal import Decimal, getcontext
# # def decimal_average(number_list, signs_count):
# #     getcontext().prec = signs_count
# #     return Decimal(sum(number_list)) / Decimal(len(number_list))
# def decimal_average(number_list, signs_count):
#     dec_list = [Decimal(i) for i in number_list]
#     print(dec_list)
#     getcontext().prec = signs_count
#     average = sum(dec_list) / Decimal(len(dec_list))
#     return average
#
#
# print(decimal_average([4.5788689699797, 34.7576578697964, 86.8877666656633, 12], 6))

#
# import collections
#
# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
#
#
# def convert_list(cats):
#     new_list = []
#     for i in cats:
#         if isinstance(i, tuple):
#             new_list.append({"nickname": i.nickname, "age": i.age, "owner": i.owner})
#         if not isinstance(i, tuple):
#             cat = Cat(**i)
#             new_list.append(cat)
#     return new_list
#
#
# print(convert_list([{"nickname": 'Mick', "age": 5, "owner": 'Sara'},
#                    {"nickname": 'Barsik', "age": 7, "owner": 'Olga'},
#                    {"nickname": 'Simon', "age": 3, "owner": 'Yura'}]))
# # print(convert_list([Cat(nickname='Mick', age=5, owner='Sara'),
# #                     Cat(nickname='Barsik', age=7, owner='Olga'),
# #                     Cat(nickname='Simon', age=3, owner='Yura')]))

#
# from collections import Counter
#
#
# def get_count_visits_from_ip(ips):
#     ips_counts = Counter(ips)
#     return ips_counts
#
#
# def get_frequent_visit_from_ip(ips):
#     ips_counts = Counter(ips)
#     return ips_counts.most_common(1)[0]
#
#
# print(get_count_visits_from_ip(['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114',
#                           '76.98.129.245', '66.50.38.43', '248.95.93.236', '173.37.214.238',
#                           '76.98.129.245', '76.98.129.245', '85.157.172.253', '66.50.38.43',
#                           '66.50.38.43', '66.50.38.43']))
# get_frequent_visit_from_ip(['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114',
#                           '76.98.129.245', '66.50.38.43', '248.95.93.236', '173.37.214.238',
#                           '76.98.129.245', '76.98.129.245', '85.157.172.253', '66.50.38.43',
#                           '66.50.38.43', '66.50.38.43'])
#
#
# from collections import deque
#
#
# MAX_LEN = 5
#
# lifo = deque(maxlen=MAX_LEN)
#
#
# def push(element):
#     return lifo.appendleft(element)
#
#
# def pop():
#     return lifo.popleft()
#
#
# print(lifo)
# push("Bob")


from collections import deque


MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)


def push(element):
    return fifo.append(element)


def pop():
    return fifo.popleft()

