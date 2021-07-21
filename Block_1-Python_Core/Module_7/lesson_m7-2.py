# login = input(": ")
# password = input(": ")
# c = 0
# with open('test.txt', 'r') as f:
#     for line in f:
#         parts = line.split(" ")
#         if parts[0] == login and parts[1][:-1] == password:
#             print("Access")
#             c = 1
#             break
#     if not c:
#         print("Wrong")
#
#
#
# from setuptools import setup
#
#
# def do_setup(args_dict):
#     setup(
#         name=args_dict["name"],
#         version=args_dict["version"],
#         description=args_dict["description"],
#         url=args_dict["url"],
#         author=args_dict["author"],
#         author_email=args_dict["author_email"],
#         license=args_dict["license"],
#         packages=args_dict["packages"]
#     )
#     return setup
#
#
# from setuptools import setup, find_namespace_packages
#
#
# def do_setup(args_dict, requiers):
#       setup(name=args_dict['name'],
#             version=args_dict['version'],
#             description=args_dict['description'],
#             url=args_dict['url'],
#             author=args_dict['author'],
#             author_email=args_dict['author_email'],
#             license=args_dict['license'],
#             packages=args_dict['packages'],
#             install_requires=requiers)
#

#
# from setuptools import setup, find_namespace_packages
#
#
# def do_setup(args_dict,requiers,entry_points):
#       setup(name=args_dict['name'],
#             version=args_dict['version'],
#             description=args_dict['description'],
#             url=args_dict['url'],
#             author=args_dict['author'],
#             author_email=args_dict['author_email'],
#             license=args_dict['license'],
#             packages=args_dict['packages'],
#             install_requires=requiers,
#             entry_points={'console_scripts': ['helloworld = clean_folder.some_code:hello_world']})
#
#
# def is_integer(s):
#     if len(s) == 0 or s == " ":
#         return False
#     if s in "abcdefghijklmnopqrstuvwxyz":
#         return False
#     return True

#
# import re
#
#
# def capital_text(s: str):
#     s = s.lstrip()
#     s = s[0].upper() + s[1:]
#     result = re.findall(r'\.\s?\w|\!\s?\w|\?\s?\w', s)
#     for i in result:
#         s = s.replace(i, i[:-1] + i[-1].upper())
#
#     return s

#
# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     result = ""
#     if reverse == False:
#         index = riddle.index(start_letter)
#         print(index)
#         result += riddle[index:word_length + index]
#         print(result)
#         return result
#     elif reverse == True:
#         index = riddle.index(start_letter)
#         print(index)
#         result += riddle[index:index-word_length:-1]
#         print(result)
#         return result
#
#
# solve_riddle('mi1powperet', 3, 'r', reverse=True)
# solve_riddle("milpowerpret", 5, "p", reverse=False)


#
# def data_preparation(list_data):
#     result = []
#     for i in list_data:
#         if len(i) > 2:
#             i.remove(max(i))
#             i.remove(min(i))
#         for j in i:
#             result.append(j)
#     result.sort(reverse=True)
#     print(result)
#     return result
#
#
# data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]])

#
# def token_parser(s):
#     s1 = s.split()
#     s2 = []
#     for i in s1:
#         if len(i) > 1 and not i.isdigit():
#             for j in i:
#                 s2.append(j)
#         if len(i) == 1 or i.isdigit():
#             s2.append(i)
#     print(s2)
#     return s2
#
#
# token_parser("2+ 34 - 5 * 3")
#
#
# def all_sub_lists(data):
#     worked_data = data.copy()
#     main_list = [[]]
#     for i in worked_data:
#         main_list.append([i])
#     for i in range(len(worked_data)):
#         main_list.append(worked_data[:2])
#         worked_data = worked_data[1:]
#         if len(worked_data) == 1:
#             break
#     return print(main_list + [data])
#
#
# all_sub_lists([4, 6, 1, 3])
#
#
# def make_request(keys, values):
#     result = dict(zip(keys, values))
#     empty_result = {}
#     if len(keys) != len(values):
#         return empty_result
#     print(result)
#     return result
#
#
# make_request(['name', 'age', 'email'], ['Nick', '23', 'nick@test.com'])
#
#
# def sequence_buttons(string):
#     string1 = string.upper()
#     result = ""
#     buttons = {"1": ".,?!", "2": "ABC", "3": "DEF", "4": "GHI", "5": "JKL",
#                "6": "MNO", "7": "PQRS", "8": "TUV", "9": "WXYZ", "0": " "}
#     for i in string1:
#         for key, value in buttons.items():
#             if i in value:
#                 result += key * (value.index(i) + 1)
#     return result
#
#
# print(sequence_buttons("Hello!"))

#
# def file_operations(path, additional_info, start_pos, count_chars):
#     with open(path, 'a') as f:
#         f.write(additional_info)
#
#     with open(path, 'r') as f:
#         f.seek(start_pos)
#         line = f.read(count_chars)
#     return line
#

#
# def get_employees_by_profession(path, profession):
#     names = ''
#     with open(path, 'r') as file:
#         lines = file.readlines()
#         for item in lines:
#             cleared_item = item.rstrip()
#             name_prof = cleared_item.split(' ')
#             if name_prof[1] == profession:
#                 names += name_prof[0]
#     return names
#
#


# def to_indexed(start_file, end_file):
#     with open(start_file, 'r') as file_start:
#         lines = file_start.readlines()
#         count = 0
#         text_for_add = ''
#         for item in lines:
#             item = str(count) + ': ' + item
#             text_for_add += item
#             count += 1
#         with open(end_file, 'w') as f:
#             f.write(text_for_add)

# def flatten(data):
#     if len(data) < 1:
#         return []
#     elif isinstance(data[0], list):
#         first_list = flatten(data[0])
#         second_list = flatten(data[1:])
#         main_list = first_list + second_list
#     elif not isinstance(data[0], list):
#         first_list = [data[0]]
#         second_list = flatten(data[1:])
#         main_list = first_list + second_list
#     return main_list
#

#
# def decode(data):
#     if len(data) == 0:
#         return []
#     else:
#         return [i for i in data[0] * data[1]] + decode(data[2:])
#

def encode(data):
    def func(a, b=[]):
        if not a:
            return b
        else:
            if not b or b[len(b) - 2] != a[0]:
                b.append(a[0])
                b.append(1)
                return func(a[1:])
            if b[len(b) - 2] == a[0]:
                b[len(b) - 1] += 1
                return func(a[1:])
    return func(data)

