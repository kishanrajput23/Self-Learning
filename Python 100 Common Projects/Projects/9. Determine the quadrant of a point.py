x = float(input("Insert coordinate of point x: "))
y = float(input("Insert coordinate of point y: "))

if x > 0 and y > 0:
    print("The first quadrant")
elif x < 0 and y >0:
    print("The second quadrant")
elif x < 0 and y  < 0:
    print("The third quadrant")
elif x < 0 and y < 0:
    print("The forth quadrant")
elif x == 0 and y == 0:
    print("Point of origin")
elif x == 0:
    print("x point")
elif y == 0:
    print("y point")