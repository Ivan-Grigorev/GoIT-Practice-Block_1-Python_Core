l = []
for i in range(2, 11, 2):
    l.append(i)
print(l)

l = [i for i in range(1, 11) if i % 2 == 0]
print(l)

l_2 = [i if not i % 2 else 0 for i in range(1, 11)]
print(l_2)

l_3 = [0 if i % 2 else 1 for i in range(10)]
print(l_3)

l_4 = [1 if i % 2 else 0 for i in range(10)]
print(l_4)

l_5 = [i for i in range(10, 0, -1)]
print(l_5)

s = input(': ')
l_6 = [i for i in s if i in "ljldlnb.,nsssof"]
print(l_6)

l_7 = [i for i in s if i not in "ljldlnb.,nsssof"]
print(l_7)
l_8 = [i for i in s if i not in ["aaaaaaaayyyyuuuuu"]]
print(l_8)



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

def invite_to_event(username):
    return (f"Dear {username}\nwe have the honor to invite you to a unique event - \npresentation of our new carpet cleaning product.\nThe event will take place on May 13, 2023 at:\nKyiv, Svobody Avenue, 234/12 ")

print(invite_to_event("Jack"))

base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global total_trip
    total_trip += 1
    trip_price = float(base_rate + (path * price_per_km))
    return trip_price


trip_price(5)


def discount_price(price, discount):
    def apply_discount(discount):
        nonlocal price
        price = 5
        apply_discount = price - float(discount)
        return apply_discount

    apply_discount(1)
    return price

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:10:3]

numbers_copy = numbers[:]
print(numbers_copy)


alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=".")

    
# Add 5 elements to the list and remove the first and last element (removal can be done in 2 ways - functions and slice)
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

# Create list of numbers from 10 to 20
list_a = [i for i in range(10, 21)]
print(list_a)


# Calculate the sum of the numbers in the list
list_a = [i for i in range(10, 21)]
sum = 0

for i in list_a:
    sum += i
print(list_a)
print(sum)


# Create a list of lists output a list of the number 2 in each of the lists
list_a = [[1, 2], [2, 3], [5, 8], [2, 2]]
list_b = []

for i, val in enumerate(list_a):
    if 2 in val:
        i += 1
        list_b = [i]
print(list_a)
print(list_b)


# Create a list of lists output a list of indexes of lists where none 2
list_a = [[1, 2], [2, 3], [5, 8], [2, 2]]
list_b = []

for i, val in enumerate(list_a):
    if 2 not in val:
        list_b += [i]
print(list_a)
print(list_b)
