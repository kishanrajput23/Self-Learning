x = 20
y = 30
z = 40

value = input("Insert variable x,y,z only: ")

try:
    exec("print("+value+")")
except NameError:
    print("Incorrect variable name!")