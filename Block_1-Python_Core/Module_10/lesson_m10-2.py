class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        pass

    def clear(self):
        pass

    def move(self, step_x, step_y):
        self.clear()
        self.x += step_x
        self.y += step_y
        self.draw()


class Ellipse(Circle):
    def draw(self):
        super().draw()


circles = [
    Circle(10, 20, 30, "red"),
    Circle(30, 20, 10, "green")
]
for circle in circles:
    circle.draw()


#########################################

class Parent1:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"Hi! My name is {self.name}.")


class Parent2:
    def __init__(self):
        print("This is parent2")


class Child(Parent1, Parent2):
    def __init__(self, name, age):
        super(Parent1, self).__init__(name)
        super(Parent2, self).__init__()
        self.age = age


child = Child("Joe", 15)
child.say_name()

#########################################

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


animal = Animal("Ted", 5)

###################################

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


animal = Animal("Simon", 10)
animal.change_weight(12)

####################################

class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        self.color = color
        Animal.color = color


first_animal = Animal("Simon", 10)
first_animal.change_color("red")

second_animal = Animal("Ted", 5)
second_animal.change_color("red")

print(Animal.color)

########################################

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


cat = Cat("Simon", 10)
print(cat.say())

########################################

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        self.breed = breed
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"


dog = Dog("Barbos", 23, "labrador")
print(dog.nickname)
print(dog.weight)
print(dog.breed)

########################################

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {"name": self.name, "age": self.age, "address": self.address}
        #  return {"name": owner.name, "age": owner.age, "address": owner.address}


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.nickname = nickname
        self.weight = weight
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def who_is_owner(self):
        return Owner.info(self.owner)

    def say(self):
        return "Woof"


owner = Owner("Sherlock", 24, "London, 221B Baker Street")
dog = Dog("Barbos", 10, "british", owner)
print(dog.who_is_owner())

###########################################

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"


c_d = CatDog("Simon", 10)
d_c = DogCat("Barbos", 10)
print(c_d.say())
print(d_c.say())
print(c_d.info())
print(d_c.info())

#############################################

from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        return list(filter(lambda x: self.data[x] == value, self.data))


#############################################

from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum(filter(lambda x: x > 0, self.data))

#############################################

from collections import UserString
import re


class NumberString(UserString):
    def number_count(self):
        count = 0
        string = re.findall('\d+', self.data)
        for i in string:
            for j in i:
                count += 1
        return count


cl_string = NumberString("The resulting profit was: from the southern possessions $123,"
                         "from the northern colonies $45, and the king gave $67890.")
print(cl_string.number_count())

########################################

class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith("01"):
        raise IDException
    else:
        id_list.append(employee_id)
        return id_list

#########################################

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return 'Meow'

    def change_weight(self, weight):
        self.weight = weight

#########################################

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({"id": Contacts.current_id, "name": name,
                              "phone": phone, "email": email, "favorite": favorite})
        Contacts.current_id += 1

##########################################

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({"id": Contacts.current_id, "name": name,
                              "phone": phone, "email": email, "favorite": favorite})
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for i in self.contacts:
            for j in i.values():
                if j == id:
                    return i
                else:
                    return None
        # result = list(filter(lambda contact: contact.get("id") == id,
        #                      self.contacts))
        # return result[0] if len(result) > 0 else None

####################################

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({"id": Contacts.current_id, "name": name,
                              "phone": phone, "email": email, "favorite": favorite})
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id,
                             self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        result = list(filter(lambda contact: contact.pop("id") == id,
                             self.contacts))
        if result[0] in self.contacts:
            self.contacts.remove(result[0])

#########################################
