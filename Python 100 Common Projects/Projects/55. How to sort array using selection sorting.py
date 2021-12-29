from random import randint

x = 20
y = []

for i in range(20):
    y.append(randint(1,20))
print(y)

j = x-1
while j != 0:
    k = 0
    for i in range(1, j+1):
        if y[i] > y[k]:
            k = i
    z = y[k]
    y[k] = y[j]
    y[j] = z
    j -= 1
print(y)