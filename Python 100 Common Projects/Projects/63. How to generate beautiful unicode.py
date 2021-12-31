Unicode = {0: 9471, 1: 10102, 2: 10103, 3: 10104,
          4: 10105, 5: 10106, 6: 10107, 7: 10108,
          8: 10109, 9: 10110,10: 10111}

x = input("Insert digits 0-9: ")
num = " "

for i in x:
    i = int(i)
    i = chr(Unicode[i])
    num = num + i

print("The result of Unicode = %s" % num)