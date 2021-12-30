from random import randint

row = 5
matrix = []

for i in range(row):
    myrow = []
    for j in range(row):
        myrow.append(randint(1,100))
        print("%4d" % myrow[j], end=' ')
    matrix.append(myrow)
    print()
print()

for i in range(row):
    x = matrix[i][i]
    matrix[i][i] = matrix[i][row-1-i]
    matrix[i][row-1-i] = x

for i in matrix:
    for j in i:
        print("%4d" % j, end=' ')
    print()

