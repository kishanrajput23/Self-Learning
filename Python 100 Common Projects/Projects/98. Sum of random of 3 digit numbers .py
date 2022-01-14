from random import random

x = random()*900+100
x = int(x)
print(x)

s = str(x)

y = int(s[0])#x//100
z = int(s[1])#(x//10)%10
w = int(s[2])#x % 10

print(y+z+w)