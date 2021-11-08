x = abs(int(input("Choose the element to find its value: ")))

f1 = f2 =1
y = 2

while y < x:
    f1, f2 = f2, f1+f2
    y += 1
print("The value of the ",x," elemnent is =", f2)