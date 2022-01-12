x = float(input("Insert first number: "))
y = float(input("Insert second number: "))

try:
    z = x/y
except ZeroDivisionError:
    print("Error! Number not divisible by zero...")
else:
    print(z)