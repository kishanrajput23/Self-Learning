from random import  random

x = 20
y = []

for i in range(x):
    y.append(random())
    print(round(y[i],2), end=' ')
print()

maximum = 0
for i in y:
    if i > maximum:
        maximum = i
print("The maximum value = ", round(maximum,2))