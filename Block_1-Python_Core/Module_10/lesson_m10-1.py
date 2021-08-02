############################################
#
# create class Rectangle with 2 sides and area and perimeter methods
#
class Rectangle:
    def __init__(self, s1, s2):
        self.a = s1
        self.b = s2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


rec1 = Rectangle(5, 4)
print("Perimeter:", rec1.perimeter())
print("Area:", rec1.area())

rec2 = Rectangle(5, 2)
print("Perimeter:", rec2.perimeter())
print("Area:", rec2.area())
#
#############################################
#
# class Node of binary tree
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
#
#############################################
#
class Human:
    name = ''

    def voice(self):
        print(f"Hello! My name is {self.name}")


class Developer(Human):
    field_description = "My Programming language"
    value = ""

    def make_some_code(self):
        return f"{self.field_description} is {self.value}"


class PythonDeveloper(Developer):
    name = "Slava"
    value = "Python"

    def voice(self):
        print(f"Hello! I'm {self.name}")


class JSDeveloper(Developer):
    value = "JavaScript"


p_dev = PythonDeveloper()
p_dev.voice()   # Hello! My name is Bob
print(p_dev.make_some_code())  # My Programming language is Python


js_dev = JSDeveloper()
js_dev.name = "Bob"
js_dev.voice()
print(js_dev.make_some_code())  # My Programming language is JavaScript

c_dev = Developer()
c_dev.value = "c"
print(c_dev.make_some_code())
#
#################################################
#
class Mammal:
    phrase = ''

    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'


class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'Whooooo!!!'


class Person:
    phrase = "Hello, World!"


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


def example_func(animal):
    a = animal()
    print(a.phrase)


rec = Recorder

r = rec()
cat = Cat()
dog = Dog()
example_func(Cat)
person = Person()
strange_animal = Chupakabra()

r.record_animal(cat)            # Recorded "Meow!"
r.record_animal(dog)            # Recorded "Bark!"
r.record_animal(strange_animal) # Recorded "Whooooo!!!"
#
#############################################
#
class First(object):
    y = "First!!!"
    v = "v from First!"


class A(First):
    d = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exist only in B'


class C(A, B):
    z = "This exists only in C"


c = C()
print(c.z)  # This exists only in C
print(c.y)  # I exist only in B
print(c.x)  # I am A class
print(c.v)
print(c.d)
#
################################################
#
# create a Shape class: rectangle, triangle and circle. The shape sides it`s list and the methods is area.
# This arguments overridden and added to tittle.
#
from cmath import pi


class Figure:
    sides = []

    def area(self):
        return "Some area"

    def get_sides(self):
        return self.sides

    def set_sides(self, list_of_sides):
        self.sides = list_of_sides


class Rectangle(Figure):
    sides = [1, 2]

    def area(self):
        return self.sides[0] * self.sides[1]


class Circle(Figure):
    radius = 5

    def area(self):
        return pi * (self.radius ** 2)


class SomeFigure(Figure):
    sides = [3, 5, 3, 2, 7]


c = Circle()
c.radius = 7
print(c.sides)
print(c.radius)
print(c.area())

r = Rectangle()
print(r.sides)
print(r.area())

sm = SomeFigure()
print(sm.sides)
print(sm.area())
#
########################################
#
# write addition to dictionary - the function checking the value in keys and values
#
from collections import UserDict


class ValueSearchableDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values() or value in self.data.keys()


as_dict = ValueSearchableDict()
as_dict[1] = 2

print(as_dict.has_in_values(1))    # True
print(as_dict.has_in_values(2))
#
#########################################
#
import string
import module


class NameTooShortError(Exception):
    print('Name is too short, need more than 3 symbols. Try again.')


class NameStartsFromLowError(Exception):
    print('Name should start from capital letter. Try again.')


def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


ch = 0
while ch < 3:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        ch += 1
    except NameStartsFromLowError:
        ch += 1
print("YYYYY")
#
##########################################
