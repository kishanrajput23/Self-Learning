import random

x = []
for i in range(20):
    x.append(int(random.random()*20)-10)
print(x)

pos = []
neg = []

for i in x:
    if i<0:
        neg.append(i)
    elif i>0:
        pos.append(i)
print("Negative numbers = ",neg)
print("Positive numbers = ",pos)