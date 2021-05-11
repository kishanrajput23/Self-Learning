print("Insert lenght of proposed triangle: ")
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

if x+y>z and x+z>y and y+z>x:
    print("The triangle of xyz exist")
else:
    print("The triangle does not exist")