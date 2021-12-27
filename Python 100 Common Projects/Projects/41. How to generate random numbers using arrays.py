from random import randint

x = 20
array = []

for i in range(x):
    array.append(randint(1,10))
for i in array:
    print(i,end=' ')
print()