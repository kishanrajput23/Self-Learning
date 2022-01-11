x = input("Insert numbers only: ")

while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print("Error! Please insert only numbers...")
        x = input("Insert numbers only: ")
print(x/2)