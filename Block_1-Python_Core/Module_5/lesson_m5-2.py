import re


string = "Niels Bohr was born in the family of a professor of physiology at the University of Copenhagen, Christian Bohr (1858-1911)," \
          "twice nominated for the Nobel Prize in Physiology or Medicine[10], and Ellen Adler" \
          "(1860-1930), daughter of an influential and very wealthy Jewish banker and liberal parliamentarian David" \
          "Baruch Adler (Dan. David Baruch Adler; 1826-1878) and Jenny Raphael (1830-1902) from the British Jewish" \
          "of the banking dynasty Raphael Raphael & sons[en][11]. Bor's parents married in 1881."

pattern = r'\d+'
result = re.search(pattern, string)
# print(result.span())
# print(result.group())
# print(result.string)

pattern = r'\d+'
result = len(re.findall(pattern, string))
print(result)


def count_numbers(string):
    return len(re.findall(r'\d', string))

result = count_numbers(string)
print(result)

result = re.findall(r'[0-9]{4}', string)
print(result)

pattern = r'[А-Я]'
new_pattern = re.compile(pattern)
result = new_pattern.findall(string)
print(result)

##############

import re


google_url = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"
rozetka_url = "kolichestvo-osnovnih-kamer=3630921;producer=xiaomi;23777=6-6-5;38435=677049"


def get_object_parameters(query, pattern="&|;", key_split="="):
    object_search = {}
    for el in re.split(pattern, query):
        key, value = el.split(key_split)
        object_search.update({key: value.replace("+", " ")})
    return object_search


print(get_object_parameters(google_url))
print(get_object_parameters(rozetka_url))

################

import re


string = "Exclude from this [group string] the characters [between] brackets [, ]."

lang = "The best language Java"
pattern = "Java"

result = re.sub(pattern, "Python", lang)
print(result)

pattern = r"\[.*?\]"
result = re.sub(pattern, "", string)
print(result)

################

import re


string = "Niels Bohr was born in the family of a professor of physiology at the University of Copenhagen, Christian Bohr (1858-1911)," \
          "twice nominated for the Nobel Prize in Physiology or Medicine[10], and Ellen Adler" \
          "(1860-1930), daughter of an influential and very wealthy Jewish banker and liberal parliamentarian David" \
          "Baruch Adler (Dan. David Baruch Adler; 1826-1878) and Jenny Raphael (1830-1902) from the British Jewish" \
          "of the banking dynasty Raphael Raphael & sons[en][11]. Bor's parents married in 1881."

# print(re.findall(r'[^\w]', string))

# print(re.findall(r'^\w+', string))
# print(re.findall(r'(\w+)\.?$', string))

# pattern = r"[А-Яа-я]{3}\b"
# print(re.findall(pattern, string))

# pattern = r"\b\d{3}"
# print(re.findall(pattern, string))

# print(re.findall(r"\d{4}—\d{4}", string))
# print(re.findall(r"\d{4}—(\d{4})", string))
# print(re.findall(r"(\d{4})—\d{4}", string))
# print(re.findall(r"(\d{4})—(\d{4})", string))

result_list = []
iterator = re.finditer(r"\d{4}—\d{4}", string)
for match in iterator:
    result_list.append(match.group())
print(result_list)

text = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.net "

print(re.findall(r"@\w+\.\w{2,5}", text))
print(re.findall(r"@\w+\.(\w{2,5})", text))

################

map = {ord('з'): 'z', ord('ю'): 'uu'}
translated = 'p.зюзюыызю'.translate(map)
print(translated)  # zu

symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]

MAP = {}

print(zip(symbols, code))

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

result = "34 DF 56 AC".translate(MAP)
print(result)

#################

def real_len(text):
    text_list = list(text)
    result = []
    print(text_list)
    for i in text_list:
        if i != '\n' and i != '\f' and i != '\r' and i != '\t' and i != '\v':
            result.append(i)
    print(result)
    print(len(result))
    return len(result)


real_len('gdgd\n\t')

##################

articles_dict = [
    {
        "title": "Minim voluptate eu aliqua duis pariatur cupidatat voluptate.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Dolore Lorem aliquip est labore elit labore ex consequat ad occaecat duis.",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "Aliqua minim amet ut pariatur et occaecat esse qui commodo ut duis sunt elit.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "Irure reprehenderit aliquip officia quis occaecat aute mollit laborum ullamco laboris Lorem commodo.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    coincidence = False
    new_list = []
    if letter_case:
        for i in articles_dict:
            for j in i.values():
                try:
                    if j.find(key) != -1:
                        coincidence = True
                except:
                    continue
            if coincidence:
                new_list.append(i)
            coincidence = False
    else:
        for i in articles_dict:
            for j in i.values():
                try:
                    key.upper()
                    j.upper()
                    if j.find(key) != -1:
                        coincidence = True
                except:
                    continue
            if coincidence:
                new_list.append(i)
            coincidence = False

    return new_list
  
##################

def sanitize_phone_number(phone):
    new_phone = (phone.strip()
                 .removeprefix("+")
                 .replace("(", "")
                 .replace(")", "")
                 .replace(" ", "")
                 .replace("-", ""))
    print(new_phone)
    return new_phone


sanitize_phone_number("    +38(050)123-32-34")

##################

def is_check_name(fullname, first_name):
    if first_name in fullname:
        return True
    for i in fullname:
        if i.isupper():
            return False
    else:
        return True


def sanitize_phone_number(phone):
    new_phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
            .replace("+", "")
        )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    ua = []
    jp = []
    tw = []
    sg = []
    result = dict(UA=ua, JP=jp, TW=tw, SG=sg)
    list_phones1 = str(list_phones)
    list_phones2 = sanitize_phone_number(list_phones1)
    if list_phones2.startswith('380'):
        ua.append(list_phones2)
    if list_phones2.startswith('81'):
        jp.append(list_phones2)
    if list_phones2.startswith('886'):
        tw.append(list_phones2)
    if list_phones2.startswith('65'):
        sg.append(list_phones2)
    if not list_phones2.startswith('380')\
            and not list_phones2.startswith('81')\
            and not list_phones2.startswith('886')\
            and not list_phones2.startswith('65'):
        ua.append(list_phones2)
    return print(result)


get_phone_numbers_for_countries(["+380508509978", "+380509002254", "+886509002254", "+444509002254"])

####################

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


def get_phone_numbers_for_countries(list_phones):
    phone_dict = {'JP':[], 'SG':[], 'TW':[], "UA":[]}
    for i in list_phones:
        sannumber = sanitize_phone_number(i)
        if sannumber.startswith('380'):
            phone_dict['UA'].append(sannumber)
        elif sannumber.startswith('81'):
            phone_dict['JP'].append(sannumber)
        elif sannumber.startswith("65"):
            phone_dict['SG'].append(sannumber)
        elif sannumber.startswith('886'):
            phone_dict['TW'].append(sannumber)
        else:
            phone_dict['UA'].append(sannumber)
    return phone_dict


print(get_phone_numbers_for_countries(["+380508509978", "+380509002254", "+886509002254", "+444509002254"]))

##################

def is_spam_words(text, spam_words, space_around=False) -> bool:
    spam_words = str()
    for spam_words in text:
        space_terms = text.index(spam_words) == 0 or spam_words.find(" ") \
                       and spam_words.rfind(".") or spam_words.rfind(" ")
        if spam_words in text and spam_words != space_terms and space_around == False:
            return True
    for spam_words in text:
        space_terms = text.index(spam_words) == 0 or spam_words.find(" ") \
                       and spam_words.rfind(".") or spam_words.rfind(" ")
        if spam_words in text and spam_words == space_terms and space_around == True:
            return False
    else:
        return False


print(is_spam_words("Молох", ["лох"]))
print(is_spam_words("Молох", ["лох"], True))

##################

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l",
               "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch",
               "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for i, j in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(i)] = j
    TRANS[ord(i.upper())] = j.upper()


def translate(name):
    return name.translate(TRANS)


print(translate("Дмитрий Коробов"))
print(translate("Александр Иванович"))

####################

grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    counter = 0
    for key, value in students.items():
        for i, j in grade.items():
            if value == i:
                counter += 1
                print("{:>4}|{:<10}|{:^5}|{:^5}".format(counter, key, i, j))
    return


formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"})

####################

grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    count = 0
    new_list = []
    for i, j in students.items():
        for x, z in grade.items():
            if j == x:
                count += 1
                spisok = '{:>4}|{:<10}|{:^5}|{:^5}'.format(count, i, x, z)
                new_list.append(spisok)
    return new_list


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

print(formatted_grades(students))

#####################

def formatted_numbers():
    num_list = []
    table_title = "|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')
    num_list.append(table_title)
    for i in range(16):
        num_str = "|{0:<10d}|{0:^10x}|{0:10b}|".format(i)
        num_list.append(num_str)
    return num_list


print(formatted_numbers())

#####################

import re


def find_word(text, word):
    if word in text:
        search = re.search(word, text)
        result1 = {'result': True, 'first_index': search.start(), 'last_index': search.end(),
                       'search_string': word, 'string': text}
        return result1
    elif word not in text:
        result2 = {'result': False, 'first_index': None, 'last_index': None,
                        'search_string': word, 'string': text}
        return result2


print(find_word("Guido van Rossum began working on Python in the late 1980s,"
                " as a successor to the ABC programming language, and first"
                " released it in 1991 as Python 0.9.0.", "Python"))

#####################

import re


def find_all_words(text, word):
    if word in text:
        result = re.findall(word, text, re.IGNORECASE)
        return result

#####################

import re


def replace_spam_words(text, spam_words):
    for i in spam_words:
        star = "*" * len(i)
        result = re.sub(i, repl=star, string=text, flags=re.IGNORECASE)
        text = result
    return result


print(replace_spam_words("Guido van Rossum began working on Python in the late 1980s,\n"
                "as a successor to the ABC programming language,\n"
                "and first released it in 1991 as Python 0.9.0.", ["began", "Python"]))

#####################

import re


def find_all_emails(text):
    #result = re.findall(r"[A-z]+[a-zA-Z0-9._]+@[a-z]+.[a-z]\w{2,}", text)
    result = re.findall(r"[a-zA-z][a-zA-Z0-9_.]+@[a-z]+\.\w{2,4}", text)
    print(result)
    return result


find_all_emails('ma@Foolrg Ima.Fool@iana.o 1Fool@iana.org'
                'first_last@iana.org first.middle.last@iana.or A_a@test.com abc111@test.com.net')

######################

import re


def find_all_phones(text):
    result = re.findall(r"\+380?\(?\d{2}\)?\d{3}[\s\-]\d{2}[\s\-]\d{2}|"
                        r"\+380?\(?\d{2}\)?\d{3}[\s\-]\d{1}[\s\-]\d{3}", text)
    print(result)
    return result


find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77'
                 ' aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787')

###################

import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"https?:\/\/\w*\.?(\w+\.)+\w{2,5}", text)
    for match in iterator:
        result.append(match.group())
    print(result)
    return result


find_all_links('The main search site in the world is https://www.google.com'
               ' The main social network for people in the world is https://www.facebook.com'
               ' But programmers have their own social network http://github.com'
               ' There they share their code. some url to check https://www..facebook.com www.facebook.com')
