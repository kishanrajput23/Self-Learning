import math

x = float(input("Insert point x: "))
y = float(input("Insert point y: "))
r = float(input("Insert the radius: "))

hypotenuse = math.sqrt(pow(x,2) + pow(y,2))

if hypotenuse <= r:
    print("The point belongs to circle.")
else:
    print("The point does not belong to circle.")