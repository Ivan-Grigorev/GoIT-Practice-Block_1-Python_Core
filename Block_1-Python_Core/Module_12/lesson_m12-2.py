from copy import deepcopy, copy


class Container:
    def __init__(self, name):
        self.data = []
        self.name = name

    def append(self, item):
        self.data.append(item)

    def __copy__(self):
        copy_obj = Container(self.name)
        copy_obj.data = copy(self.data)
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Container(self.name)
        memo[id(copy_obj)] = copy_obj
        copy_obj.data = deepcopy(self.data)
        return copy_obj


if __name__ == "__main__":
    container1 = Container("original")

    container1.append("This is a test string")
    container1.append(["Some data", "42"])

    print(container1.data)

    container2 = copy(container1)
    container3 = deepcopy(container1)

    print(container2.data)

    container1.data[-1].append("Very strange text")

    print(container1.data)
    print(container2.data)
    print(container3.data)

    print(10 * "=")

    container3.append([1, 1, 2, 3, 5])

    print(container1.data)
    print(container2.data)
    print(container3.data)

###################################
def my_sum(*args, **kwargs):
    s = 0
    for value in args:
        s += value
    for value in kwargs.values():
        s += value
    return s


if __name__ == "__main__":
    print(my_sum(2, 2, 3, 4, 5, 100000, value=100, value2=200))

###################################
import csv


class Contacts:

    def __init__(self, path):
        self.path = path
        self.list_contact = []

    def load(self):
        with open(self.path, 'r') as fh:
            for line in fh:
                contact = line.split(';')
                if len(contact) > 3 and contact[3].removesuffix('\n').isdigit():
                    self.list_contact.append(contact[3].removesuffix('\n'))
            return self.list_contact

    def sanitize_phone_38(self):
        return [contact.removeprefix("38") for contact in self.list_contact]

    def sanitize_phone_00(self):
        return [contact.removeprefix("00") for contact in self.list_contact]

    def delete_duplicate(self):
        return list(set(self.list_contact))

    def invalid_list(self):
        return [contact for contact in self.list_contact if len(contact) < 10]

    def intersection_func(self, other):
        return list(set(self.list_contact) & set(other.list_contact))

    def int_difference_func(self, other):
        difference = set(self.list_contact) - set(other.list_contact)
        with open('int_contact.csv', 'w', newline='\n') as file:
            writer = csv.writer(file, delimiter=';')
            for phone in difference:
                writer.writerow(phone)
        return list(difference)

    def ext_difference_func(self, other):
        difference = set(other.list_contact) - set(self.list_contact)
        with open('ext_contact.csv', 'w', newline='\n') as file:
            writer = csv.writer(file, delimiter=';')
            for phone in difference:
                writer.writerow(phone)
        return list(difference)

    @staticmethod
    def _write_phone(file, phone):
        with open(file, "w+", newline="") as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(phone)

    def dump_operators(self, other):
        new_list = self.list_contact + other.list_contact
        vodafone_codes = ["050", "095", "099", "066"]
        kyivstar_codes = ["067", "096", "097", "098", "039"]
        lifecell_codes = ["063", "073", "091", "092", "094"]

        for phone in new_list:
            if phone[:3] in kyivstar_codes:
                self._write_phone(phone, "kyivstar.csv")
            elif phone[:3] in vodafone_codes:
                self._write_phone(phone, "vodafone.csv")
            elif phone[:3] in lifecell_codes:
                self._write_phone(phone, "lifecell.csv")

    @staticmethod
    def save_file(path_for_save, data):
        with open(path_for_save, 'w', newline='\n') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([data])
        print('File was written successfully')


event = Contacts('contacts_base.csv')

print(event.load())
print(event.sanitize_phone_38())
print(event.sanitize_phone_00())
print(event.delete_duplicate())
print(event.invalid_list())

bot = Contacts('bot.csv')
bot.load()


for sanitized_contact in bot.sanitize_phone_38():
    print(sanitized_contact)


print(bot.sanitize_phone_00())
print(bot.delete_duplicate())
print(bot.invalid_list())

print(event.intersection_func(bot))
print(event.int_difference_func(bot))
print(event.ext_difference_func(bot))

event.dump_operators(bot)

event.save_file("test.csv", event.invalid_list())

##################################
import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as fh:
        pickle.dump(contacts, fh)


def read_contacts_from_file(filename):
    with open(filename, "rb") as fh:
        unpacked = pickle.load(fh)
        return unpacked

#################################
import json


def write_contacts_to_file(filename, contacts):
    some_data = {}
    some_data["contacts"] = contacts
    with open(filename, "w") as fh:
        json.dump(some_data, fh)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        unpacked = json.load(fh)
        return unpacked["contacts"]

#################################
import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline='') as fh:
        field_names = ["name", "email", "phone", "favorite"]
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for value in contacts:
            writer.writerow({'name': value['name'], 'email': value['email'],
                             'phone': value['phone'], 'favorite': value['favorite']})


def read_contacts_from_file(filename):
    with open(filename, "r", newline='') as fh:
        reader = csv.DictReader(fh)
        contacts = []
        for row in reader:
            result = {"name": row["name"], "email": row["email"],
                      "phone": row["phone"], "favorite": eval(row["favorite"])}
            contacts.append(result)
        return contacts

################################
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        else:
            self.filename = filename
            self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, "wb") as fh:
            pickle.dump(self, fh)

    def read_from_file(self):
        with open(self.filename, "rb") as fh:
            unpacked = pickle.load(fh)
            return unpacked


contacts = [Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992)914-3792", False),
            Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294)840-6685", False)]
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)
print(persons.contacts[0] == person_from_file.contacts[0])
print(persons.contacts[0].name == person_from_file.contacts[0].name)
print(persons.contacts[0].email == person_from_file.contacts[0].email)
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)

####################################
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] += 1
        return attributes


contacts = [Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992)914-3792", False),
            Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294)840-6685", False)]
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)
print(first.count_save)
print(second.count_save)
print(third.count_save)

#######################################
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


contacts = [Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992)914-3792", False),
            Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294)840-6685", False)]
persons = Contacts("user_class.dot", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)
print(person_from_file)

##################################
import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    copy_person = copy.copy(person)
    return copy_person


person = Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False)
copy_person = copy_class_person(person)

print(copy_person == person)
print(copy_person.name == person.name)

#####################################
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)


contacts = [Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992)914-3792", False),
            Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294)840-6685", False)]
persons = Contacts("user_class.dat", contacts)
new_persons = copy_class_person(persons)
new_persons.contacts[0] = "Another name"

print(persons.contacts[0].name)
print(new_persons.contacts[0].name)

###################################
from copy import deepcopy, copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person(copy(self.name),
                          copy(self.email),
                          copy(self.phone),
                          copy(self.favorite))
        return copy_obj


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = Contacts(copy(self.filename),
                            copy(self.contacts))
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Contacts(copy(self.filename),
                            copy(self.contacts))
        memo[id(copy_obj)] = copy_obj
        copy_obj.filename = deepcopy(self.filename)
        copy_obj.contacts = deepcopy(self.contacts)
        return copy_obj

######################################
