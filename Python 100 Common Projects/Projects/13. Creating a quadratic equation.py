from math import sqrt

x = float(input("Insert x = "))
y = float(input("Insert y = "))
z = float(input("Insert z = "))

a = y*y-4*x*z

if a>0:
    x1 = (-y + sqrt(a))/(2*x)
    x2 = (-y - sqrt(a))/(2*x)
    print("x1 = %.2f; x2 = %.2f" % (x1,x2))
elif a==0:
    x1 = -y/(2*x)
    print("x1 = %.2f" % x1)
else:
    print("No roots exist")