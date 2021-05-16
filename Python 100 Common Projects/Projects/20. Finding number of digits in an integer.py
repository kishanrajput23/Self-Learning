x = int(input("Insert multiple integer numbers: "))
x = abs(x)

count = 1;
x //= 10

while x > 0:
    x//=10
    count += 1
print("The number of integer is: ",count)