from random import random

num = 20
listitem = [0]*num

for i in range(num):
    listitem[i] = int(random()*50)
print(listitem)

maxi = 1
mylength = 1
mycode = 0

for i in range(1,num):
    if listitem[i] > listitem[i-1]:
        mylength += 1
    else:
        if mylength > maxi:
            maxi = mylength
            mycode = i
        mylength = 1
print("The maximum lenght = ",maxi)
print("The ordered values are = ",listitem[mycode-maxi : mycode])