for i in range(30):
    s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
    print(s)

###############
    
width = 5
for num in range(5):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))


################
    
def sanitize(data):
    while True:
        start_index = data.find("[")
        end_index = data.find("]")
        if start_index == -1:
            break
        data = data[:start_index] + data[end_index + 1:]
    return data


print(sanitize(string))

#################

def count_digits(string):
    count = 0
    for el in string:
        if el.isdigit():
            count += 1
    return count


print(count_digits(string))


#################

def count_numbers(string):
    count = 0
    position = 0
    while position < len(string):
        if string[position].isdigit():
            while string[position].isdigit():
                print(position, string[position])
                position += 1
            count += 1
        else:
            position += 1
    return count

print(count_numbers(string))

numbers = ["123", "456", "100", "10", "13", "abc", "23a"]


################

def sanitize(data):
    result =[]
    for el in data:
        if el.isdigit():
            result.append(el)
    return result


def transform_to_int(data):
    result =[]
    for el in data:
        result.append(int(el))
    return result


sanitize_numbers = sanitize(numbers)
sanitize_numbers = transform_to_int(sanitize_numbers)

sorted_sanitize_numbers = sorted(sanitize_numbers, reverse=True)

print(max(sanitize_numbers))
print(min(sanitize_numbers))
print(sum(sanitize_numbers)/len(sanitize_numbers))

################

"""
There is a list of phones. Remove all erroneous lines and bring everyone to the same form. ["380669640547",
"0637306465", "380961935171", "632643973", "508325200", "000000000", "48730283918", "986223575", "375297947963"]
"""

phone_storage = [" 380669640547 ", " 0637306465", "380961935171", "632643973 ", "508325200 ", "000000000",
                 "48730283918",
                 "986223575", "375297947963", "38050964+05+47", "38050xxxxxxx", "+38(050)123-45-67",
                 "38(050)123 45 67"]

"""
+380501234567  + 38 code country 050 code operator tel: 1234567
"""

codes_operators = {"039", "050", "063", "066", "067", "068", "073", "091"}


def _is_valid_phone(phone):
    if len(phone) == 12:
        if phone[:2] == '38':
            if phone[2:5] in codes_operators:
                return True
            else:
                return False
        else:
            return False
    if len(phone) == 10:
        if phone[:3] in codes_operators:
            return True
        else:
            return False
    return False


def is_valid_phone(phone):
    def is_valid_operator(phone):
        if phone[:3] in codes_operators:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == '38':
                return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


def sanitize_phone(phone):
    new_phone = (phone.strip()
                 .removeprefix("+")
                 .replace("(", "")
                 .replace(")", "")
                 .replace(" ", "")
                 .replace("-", ""))
    return new_phone


# for phone in phone_storage:
#     phone = sanitize_phone(phone)
#     is_valid = is_valid_phone(phone)
#     if is_valid:
#         print("Телефон {:>12} валиден".format(phone))
#     else:
#         print("Телефон {:>12} не валиден".format(phone))

def pretty_table():
    print("|{:^14}|{:^12}|".format("Phone", "Result"))
    print("|{:^14}|{:^12}|".format("-" * 14, "-" * 12))
    for phone in phone_storage:
        phone = sanitize_phone(phone)
        is_valid = is_valid_phone(phone)
        if is_valid:
            print("|{:>14}|{:^12}|".format(phone, "valid"))
        else:
            print("|{:>14}|{:^12}|".format(phone, "invalid"))


if __name__ == "__main__":
    pretty_table()
    
################

url = "https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"

# Parse query string and turn it into a dictionary
_, query_search = url.split("?")  # ["https://www.google.com/search", "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"]
print(query_search)

list_parameters = query_search.split("&")
print(list_parameters)

object_search = {}
for el in list_parameters:
    key, value = el.split("=")
    object_search.update({key: value.replace("+", " ")})

print(object_search)

# Forming a query string
url_string = ''
for key, value in object_search.items():
    url_string = url_string + "=".join([key, value.replace(" ", "+")])
print(url_string)

"""
There is a 2 phone lists: 1 is a list of all registrations, 2 is a list of all who connected to the game.
Determine list of phones who have registered, but have not started working on site.
["380669640547", "0637306465",
"380961935171", "632643973", "508325200", "000000000", "48730283918", "986223575", "375297947963"]
["380669640547", "0637306465" "632643973", "508325200", "48730283918", "986223575"]
"""
from myphone import is_valid_phone

registration = []

for phone in ["380669640547", "0637306465", "380961935171", "632643973", "508325200", "000000000", "48730283918",
              "986223575", "375297947963"]:
    if is_valid_phone(phone):
        registration.append(phone)

connected = []

for phone in ["380669640547", "0637306465" "632643973", "508325200", "48730283918", "986223575"]:
    if is_valid_phone(phone):
        connected.append(phone)

print(registration)
print(connected)

result = list(set(registration) & set(connected))
print(result)

#################

url_rozetka = "https://rozetka.com.ua/mobile-phones/c80003/kolichestvo-osnovnih-kamer=3630921;producer=xiaomi;23777=6" \
              "-6-5;38435=677049/ "

query_url_rozetka = "kolichestvo-osnovnih-kamer=3630921;producer=xiaomi;23777=6-6-5;38435=677049"

query_rozetka = query_url_rozetka.split(";")

print(query_rozetka)

object_rozetka = {}
for el in query_rozetka:
    key, value = el.split("=")
    object_rozetka.update({key: value})

print(object_rozetka)

###############

def format_ingredients(items):
    items = ', '.join(items)
    recipe = items[::-1].replace(","[::-1], " and"[::-1], 1)[::-1]
    return recipe


print(format_ingredients(["onion", "cucumber", "apple", "holly shit", "2 pieces of something"]))

################

def lookup_key(data, value):
    result = []
    for i, j in data.items():
        if j == value:
            result.append(i)
    return result


print(lookup_key({"onion": 45}, 45))

###############

def split_list(grade):
    list_1 = []
    list_2 = []
    result = (list_1, list_2)
    if len(grade) == 0:
        return result
    average = sum(grade) / len(grade)
    for i in grade:
        if i <= average:
            list_1.append(i)
        elif i > average:
            list_2.append(i)
    print(f 'grade: {grade} | result: {result}')
    return result


split_list([11, 4, 3, 1, 6, 9, 5])

#################

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9
}


def calculate_distance(coordinates):
    key_points = []
    distance = []
    total_distance = sum(distance)
    if len(coordinates) == 0 and len(coordinates) == 1:
        return 0
    for i in coordinates:
        key_points.append(i)
        if len(key_points) == 2:
            for key, value in points.items():
                if key == key_points:
                    distance.append(value)
    return total_distance


print(calculate_distance([0, 1, 3, 2, 0, 2]))

###################

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    distance = 0
    step = []
    if len(coordinates) > 1:
        for i in coordinates[:-1]:
            step.append(sorted(coordinates[0:2]))
            coordinates = coordinates[1:]
    for i in step:
        i = tuple(i)
        if tuple(i) in points.keys():
            distance += points.get(i)
    return distance


print(calculate_distance([0, 1, 3, 2, 0, 2]))

##############

def game(terra, power):
    for i in terra:
        for e in i:
            if e <= power:
                power += e
            if e > power:
                break
    return power

###############

def is_valid_pin_codes(pin_codes):
    valid_pin_codes = []
    for i in pin_codes:
        if len(i) == 4:
            if i.isdigit():
                valid_pin_codes.append(i)
        for j in valid_pin_codes:
            if j not in pin_codes:
                return True
            else:
                return False


def is_valid_pin_codes(pin_codes):
    codes = []
    if pin_codes == []:
        return False
    for i in pin_codes:
        print(i)
        if i.isdigit() and i == str(i) and i not in codes and i != "" and len(i) == 4:
            codes.append(i)
        else:
            return False
    return True


print(is_valid_pin_codes(['1101', '9034', '0011']))
print(is_valid_pin_codes([]))

###############

from random import randint


def get_random_password():
    random_choice = []
    key = [randint(40, 126) for i in range(0, 8)]
    for j in key:
        j = chr(j)
        random_choice.append(j)
        continue
    random_password = "".join(random_choice)
    return random_password


get_random_password()

################

def is_valid_password(password):
    number = False
    high_symbol = False
    lower_symbol = False

    for i in password:
        if i in '1234567890':
            number = True
        elif i == i.upper() and i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            high_symbol = True
        elif i == i.lower() and i in 'qwertyuiopasdfghjklzxcvbnm':
            lower_symbol = True
    if number and high_symbol and lower_symbol and len(password) == 8:
        return True
    return False


print(is_valid_password('123Fa111'))

################

from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
    while True:
        unique_password = get_random_password()
        if is_valid_password(unique_password):
            return unique_password
        else:
            continue


print(get_password())

#################

"""
Write a parse_folder function, it takes a single path parameter,
which is a Path object. The function should scan the path directory
and return a tuple of two lists. The first is a list of files within a directory,
second list of directories.


def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_dir():
            folders += [i.name]
        else:
            files += [i.name]
    return files, folders
"""

print(__doc__)

###################

import sys


def parse_args():
    result = ""
    new_list = []
    for i in sys.argv:
        new_list.append(i)

    result = ' '.join(new_list[1:])
    return result
