seq1 = "spam"
seq2 = "scam"

res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)



items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, "was not found")
    else:
        print(key, "not found")

        
        
num = int(input("Enter an integer (0 for exit): "))
sum = 0

while num != 0:
    for i in range(0, num):
        sum += i
    print(sum)

    num = int(input("Enter an integer (0 for exit ): "))

    
    
message = input("Enter the message: ")
offset = int(input("Enter shift: "))
encoded_message = ""

for char in message:
    pos = ord(char)
    if 48 <= pos <= 57:
        newpos = (pos - 48 + offset) % 10 + 48
    elif 65 <= pos <= 90:
        newpos = (pos - 65 + offset) % 26 + 65
    elif 97 <= pos <= 122:
        newpos = (pos - 97 + offset) % 26 + 97
    else:
        newpos = pos
        encoded_message += chr(newpos)
print("Coded Message: ")
print(encoded_message)



pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print("Division by zero done!")


result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        wait_for_number = int(input("1: "))
        operator = str(input("2: "))
    except ValueError:
        print(f'{wait_for_number} is not "+" or "-" or "*" or "/". Try again.')
    except TypeError:
        print(f'{operator} is not a number. Try again.')
    
    if operator == "+":
        result = wait_for_number + wait_for_number
    elif operator == "-":
        result = wait_for_number - wait_for_number
    elif operator == "*":
        result = wait_for_number * wait_for_number
    elif operator == "/":
        result = wait_for_number / wait_for_number
    elif operator == "=":
        print(f"Result is {result}")
        break

        
        
result = None
operand = None
operator = None
wait_for_number = True

while True:
    result = input('Please type any number: ')
    try:
        result = float(result)
    except ValueError or TypeError:
        print(f'{result} is not a number')
    else:
        break

while True:
    operator = input("Please type any operation: ")
    if operator == "=":
        break
        result = result
    elif operator not in ["+", "-", "*", "/"]:
        print(f"Input {operator} is not an operation")
        continue
    
    operand = input("Please type any number: ")
    if operand == "=":
        break
        result = result
    
    try:
        operand = float(operand)
    except ValueError:
        print(f"Input {operand} is not a number")
        operand = input("Please type any number: ")
 #       while True:
        try:
                operand = float(operand)
        except ValueError:
                print(f"Input {operand} is not a number")
                operand = input("Please type any number: ")
                operand = float(operand)
                break
    
    if operator == "+":
        result += operand
    elif operator == "-":
        result -= operand
    elif operator == "*":
        result *= operand
    elif operator == "/":
        result /= operand
print(result)
