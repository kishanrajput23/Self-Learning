print("Zero operation terminates program!")
while True:
    o = input("Choose Opearator(+, -, *, /): ")
    if o == "0":
        break
    if o in ('+','-','*','/'):
        x = float(input("Enter the value of x = "))
        y = float(input("Enter the value of y = "))
        if o == '+':
            print("%.2f" % (x+y))
        elif o == '-':
            print("%.2f" % (x-y))
        elif o == '*':
            print("%.2f" % (x*y))
        elif o == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print("Error! Division by zero...")
        else:
            print("Invalid operator")
