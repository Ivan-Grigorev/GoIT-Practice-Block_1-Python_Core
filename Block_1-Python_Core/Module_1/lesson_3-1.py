# Display max number in 2 numbers
a = 1
b = 2

if a > b:
    print(a)
elif b > a:
    print(b)

# Dispaly numbers from 1 to 10
a = 0

for a in range(11, 20, 2):
    print(a, end=" ")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a // b =", a // b)


price = 15
money = int(input("1:"))

if money < price:
    print("You haven`t money")
elif money > price:
    print("You can buy!")


a = 0
for i in range(1, 4):
    a += i
print(a)


calculator = input("Let`s calculate.")

while calсulator != 0:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a // b =", a // b)
