from random import randint

x = 20
y = []

for i in range(20):
    y.append(randint(1,20))
print(y)

for i in range(x):
    for j in range(x-i-1):
        if y[j] > y[j + 1]:
            z = y[j]
            y[j] = y[j+1]
            y[j+1] = z
print(y)

