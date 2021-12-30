from random import random
row = 5
matrix = []

for i in range(row):
    myrow = []
    for j in range(row):
        myrow.append(int(random()*10))
    matrix.append(myrow)

for myrow in matrix:
    print(myrow)

sum_diagonal1 = 0
sum_diagonal2 = 0

for i in range(row):
    sum_diagonal1 += matrix[i][i]
    sum_diagonal2 += matrix[i][row-i-1]

print(sum_diagonal1)
print(sum_diagonal2)