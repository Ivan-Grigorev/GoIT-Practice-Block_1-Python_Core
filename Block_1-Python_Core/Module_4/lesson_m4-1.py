# Create dictionary where keys and values are integers
# Calculate sum of keys, values, all absolutely numbers
a = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
key_sum = 0

for i in a.keys():
    key_sum += i
print(key_sum)

value_sum = 0

for i in a.values():
    value_sum += i
print(value_sum)

sum_total = key_sum + value_sum
print(sum_total)


# Print values where keys are even numbers
a = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}

for key, value in a.items():
    if key % 2 == 0:
        print(value, end=",")

        
# Print the biggest key
a = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
b = [key for key, value in a.items()]
print(max(b))


# Print the value of the pair with the smallest key
a = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
b = [(key, value) for key, value in a.items()]
print(min(b))


# Delete the pair where key is 3
a = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}

for key, value in list(a.items()):
    if key == 3:
        del a[key]
print(a)


# Generate dictionary
# {1:5, 2:4, 3:3, 4:2, 5:1}
a = {key: val for key, val in enumerate(range(6, 0, -1)) if key >= 1}
print(a)

# {1:5, 2:4, 3:0, 4:2, 5:1}
print({i: 6 - i if i != 3 else 0 for i in range(1, 6)})


# Find average value all of the keys
a = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
print(sum(a.keys())/len(a))

def calc(num1, num2, sign):
    if sign == "+":
        return num1 + num2

calc(1, 2, 3)
print()

def list_sum(l1):
    s = 0
    for i in l1:
        s += i
    return s


l1 = [1, 4, 8, 4]
list_sum()


def func():
    .reverse()
        return b

a = [1, 2, 3]
func()

def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price - price * discount

    apply_discount()
    return price


def get_fullname(first_name, last_name, middle_name = " "):
    if middle_name == " ":
        return str(first_name + " " + last_name)
    else:
        return str(first_name + " " + middle_name + " " + last_name)

    get_fullname()



def format_string(string, length):

    if len(string) >= length:
        return str(string)
    elif len(string) < length:
        return str((((length - len(string)) // 2) * " ") + string)

    format_string()

def first(size, *topics):
    first_sum = size + len(topics)
    return first_sum


def second(size, **comments):
    second_sum = size + len(comments)
    return second_sum


first()
second()

def cost_delivery(quantity: int, *_, discount=0):
    if quantity == 1:
        return quantity * 5
    else:
        return (5 + (quantity - 1) * 2) * (1 - discount)


quantity = 2
print(cost_delivery(quantity, 1, 2, discount=0.5))


def cost_delivery(quantity, *_, discount=0):
    """The function returns the total shipping amount.

     The first parameter is the number of items in the order.
     The discount parameter passed by key only has the value 0 by default."""
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result


print(cost_delivery.__doc__)


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    if n == k:
        return 1
    else:
        return int(factorial(n) / (factorial(n - k) * factorial(k)))


print(number_of_groups(50, 7))



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


