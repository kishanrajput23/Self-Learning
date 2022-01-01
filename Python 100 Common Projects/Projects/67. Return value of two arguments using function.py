def avg(num1,num2):
    x = (num1+num2)/2
    return x

y = int(input("Insert first value: "))
z = int(input("Insert second value: "))

average = avg(y,z)
print(round(average,2))