import math

x = float(input("Insert length of x: "))
y = float(input("Insert length of y: "))

z = math.sqrt((pow(x,2)+pow(y,2)))

Area = (x*y)/2
Perimeter = x+y+z
print("Area of right angled triangle = %.2f" % Area)
print("Perimeter of right angled triangle = %.2f" % Perimeter)