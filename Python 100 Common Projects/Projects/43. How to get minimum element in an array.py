from random import  random

x = 20
y = []

for i in range(x):
    y.append(random())
    print(round(y[i],2), end=' ')
print()

minimum = 1

for i in y:
    if i < minimum:
        minimum = i
print("The minimum element is: ", round(minimum, 2))