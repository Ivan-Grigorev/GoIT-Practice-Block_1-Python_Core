def calc(n1, n2, sign):
    if sign == "+":
        return n1 + n2
    elif sign == "-":
        return n1 - n2
    else:
        return "Error"


def func2():
    print("rrr")

def __main__():
    print(calc(2, 2, "-"))


from calc import calc
from print_mode import print_mode
from ...lesson5.first import s

a = int(input(": "))
b = int(input(": "))
c = input(" ")
print(s)
answer = calc(a, b, c)
print_mode(a, b, c, answer)



def print_mode(n1, n2, sign, answer):
    if answer != "Error":
        print(f"{n1}{sign}{n2}={answer}")
    else:
        print(answer)



from module import func, var


def func2():
    print("I'm func2")

print(var)
func()
"2+3=5"



from first import func2
var = "hello"


def func():
    print("Hello World!")


func2()