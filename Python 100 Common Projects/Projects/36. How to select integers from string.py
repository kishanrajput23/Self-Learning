str = input("Insert strings with integer values: ")
lenstr = len(str)

mynum = []

x = 0
while x < lenstr:
    num = ""
    symbol = str[x]
    while '0' <= symbol <= '9':
        num += symbol
        x += 1
        if x<lenstr:
            symbol = str[x]
        else:
            break
    x += 1
    if num != "":
        mynum.append(int(num))
print(mynum)
