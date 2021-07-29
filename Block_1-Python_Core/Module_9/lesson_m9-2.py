# write a generator of 3 sample primes between 1 and 10 without repetitions
from random import randint
def generator():
    answer = []
    while len(answer)<10:
        print(answer)
        i = randint(1, 10)
        if i not in answer:
            yield i
            answer.append(i)

gen = generator()
k = 0
print("-------------")
next(gen)
print("-------------")
next(gen)
print("-------------")
for i in gen:
    print(k)
    k += 1
    # print(i)

###########################################

# create class Rectangle with margins of 2 sides and methods of area and perimeter

class Rectangle:
    def __init__(self, s1, s2):
        self.a = s1
        self.b = s2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


rec1 = Rectangle(5, 4)
print("Perimetr:", rec1.perimetr())
print("Area:", rec1.area())

rec2 = Rectangle(5, 2)
print("Perimetr:", rec2.perimetr())
print("Area:", rec2.area())

############################################

class Node of binary tree
class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r


def insertToNode(root, val):
    if not root: return Node(val)
    elif root.val <= val:
        root.right = insertToNode(root.right, val)
    else:
        root.left = insertToNode(root.left, val)
    return root

values = [8, 3, 6, 10, 1, 14, 13, 4, 7]
root = None
for i in values:
    root =insertToNode(root, i)

print(root.val)
print(root.left.val, end=" ")
print(root.right.val)
print(root.left.left.val, end=" ")
print(root.left.right.val, end=" ")
print(root.right.right.val)





############################################
def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "отлично",
        "B": "очень хорошо",
        "C": "хорошо",
        "D": "удовлетворительно",
        "E": "достаточно",
        "FX": "неудовлетворительно",
        "F": "неудовлетворительно",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "description":
        return get_description
    elif option == "grade":
        return get_grade
    else:
        return None


get_student_grade("description")

##########################################

DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    for key, value in customer.items():
        if key == "discount":
            discount_price = price * (1 - value)
        if key != "discount":
            discount_price = price * (1 - DEFAULT_DISCOUNT)
    return discount_price


print(get_discount_price_customer(10, {"name": "Boris"}))  #, "discount": 0.15}))

###########################################

def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

#############################################

def discount_price(discount):
    def inner(x):
        return x * (1 - discount)
    return inner


cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_05(price))
print(cost_10(price))
print(cost_15(price))

######################################

def format_phone_number(func):
    def inner(new_phone):
        new_phone = func(new_phone)
        if len(new_phone) < 12:
            new_phone = "+38" + new_phone
        if len(new_phone) == 12:
            new_phone = "+" + new_phone
        return new_phone
    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

########################################

import re


def generator_numbers(string=""):
    num_list = re.findall('\d+', string)
    for i in num_list:
        yield int(i)


def sum_profit(string):
    result = [i for i in generator_numbers(string)]
    return sum(result)
import re

num_list1 = []


def generator_numbers(string=""):
    global num_list1
    num_list = re.findall('\d+', string)
    num_list1 = []
    for i in num_list:
        num_list1.append(int(i))
    return num_list1


def sum_profit(string):
    string = generator_numbers(string)
    result = sum(num_list1)
    return result


print(sum_profit("The resulting profit was: from the southern possessions $ 10,"
           " from the northern colonies $50, and the king gave $100."))

###############################################

def normal_name(list_name):
    return [i for i in map(lambda x: x.title(), list_name)]


print(normal_name(["dan", "jane", "steve", "mike"]))

############################################

def get_emails(list_contacts):
    return [i for i in map(lambda x: x['email'], list_contacts)]


print(get_emails([{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk',
             'phone': '(992) 914-3792', 'favorite': False},
            {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca',
             'phone': '(294) 840-6685', 'favorite': False},
            {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net',
             'phone': '(542) 451-7038', 'favorite': False},
            {'name': 'Wylie Pope', 'email': 'est@utquamvel.net',
             'phone': '(692) 802-2949', 'favorite': False},
            {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com',
             'phone': '(501) 472-5218', 'favorite': False}]))

##############################################

def positive_values(list_payment):
    return [i for i in filter(lambda x: x > 0, list_payment)]


print(positive_values([100, -3, 400, 35, -100]))

############################################

def get_favorites(contacts):
    return [i for i in filter(lambda x: x['favorite'], contacts)]


print(get_favorites([{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk',
                      'phone': '(992) 914-3792', 'favorite': False},
                     {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca',
                      'phone': '(294) 840-6685', 'favorite': False},
                     {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net',
                      'phone': '(542) 451-7038', 'favorite': True},
                     {'name': 'Wylie Pope', 'email': 'est@utquamvel.net',
                      'phone': '(692) 802-2949', 'favorite': False},
                     {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com',
                      'phone': '(501) 472-5218', 'favorite': True}]))

#############################################

from functools import reduce


def sum_numbers(numbers):
    result = reduce(lambda x, y: x + y, numbers)
    return result


print(sum_numbers([3, 4, 6, 9, 34, 12]))

#############################################

from functools import reduce


def amount_payment(payment):
   pos_nums = [i for i in filter(lambda x: x > 0, payment)]
   result = reduce(lambda x, y:  x + y, pos_nums)
   return result


print(amount_payment([100, -3, 400, 35, -100]))

#############################################

USERS = {}


def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "Нет пользователя с таким именем"
        except ValueError:
            return "Дайте мне имя и телефон пожалуйста"
        except IndexError:
            return "Введите имя пользователя"
    return inner


def exit_handler(_):
    return


def unknown_cmd(_):
    return "Неизвестная команда"


def hello_handler(_):
    return "Чем я могу вам помочь?"


@error_handler
def add_user(args):
    name, phone = args
    USERS[name] = phone
    return f"Пользователь {name} добавлен"


@error_handler
def change_phone(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f"У {name} теперь телефон {phone}. Раньше был: {old_phone}"


@error_handler
def show_number(args):
    user = args[0]
    phone = USERS[user]
    result = f"{user}: {phone}"
    return result


def show_all(_):
    result = ""
    for name, phone in USERS.items():
        result += f"{name}: {phone}\n"
    return result


HANDLERS = {
    u"hello": hello_handler,
    u"good bye": exit_handler,
    u"close": exit_handler,
    u"exit": exit_handler,
    u"add": add_user,
    u"change": change_phone,
    u"show all": show_all,
    u"phone": show_number
}


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lstrip()
    try:
        handler = HANDLERS[cmd.lower()]
    except KeyError:
        if args:
            cmd = cmd + " " + args[0]
            args = args[1:]
        handler = HANDLERS.get(cmd.lower(), unknown_cmd)
    return handler, args


def main():
    while True:
        user_input = input(">")
        handler, *args = parse_input(user_input)
        result = handler(*args)
        if not result:
            print("Good bye!")
            break
        print(result)


if __name__ == "__main__":
   main()

###############################################
