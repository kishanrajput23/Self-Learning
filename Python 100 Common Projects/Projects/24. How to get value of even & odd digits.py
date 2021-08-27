x = int(input("Insert some numbers: "))

ev = 0
od = 0

while x > 0:
    if x%2 ==0:
        ev += 1
    else:
        od += 1
    x = x//10
print("Even numbers = %d, Odd numbers = %d" % (ev,od))

