from random import randint

row = 6
col = 6
x = []

for i in range(row):
    y = []
    for j in range(col):
        y.append(randint(1,100))
    x.append(y)
for i in x:
    for j in i:
        print("%3d" % j, end=' ')
    print()
