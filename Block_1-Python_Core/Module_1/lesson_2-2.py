a = int(input("Enter a: "))
b = int(input("Enter b: "))

x = - b / a
print(f" x = {round(x, 2)}")

s = (a * b) / 2
c = (a ** 2 + b ** 2)


from math import sqrt


a = float(input("Enter a: "))
b = float(input("Enter b: "))

s = (a * b) / 2  # area of triangle rectangle

c_classic = (a ** 2 + b ** 2) ** (1 / 2)
c_library_method = sqrt(a ** 2 + b ** 2)

print("Square = ", s)
print("Hipotenuza = {}".format(c_classic))


first_name = "Ivan"
last_name = "Grigorev"
full_name = first_name + " " + last_name
message = f"Dear {first_name}, we inform you\nthat you have purchased a ticket for a trip to the island of Mauritius.\nDeparture on June 31 this year.\nPlease apply for a ticket at the airport ticket office.\nPlease bring your passport for {full_name}.\nС looking forward to seeing you."
print(message)
