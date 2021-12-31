from random import random

row = 5
col = 10
matrix = []
for i in range(row):
    myrow = []
    for j in range(col):
        myrow.append(int(random()*50)+10)
    matrix.append(myrow)

for myrow in matrix:
    print(myrow)

num = int(input("Range of numbers(10-50): "))

print("Rows: ", end=' ')
for i in range(row):
    if num in matrix[i]:
        print(i,end=' ')
print()

print("Columns: ",end=' ')
for j in range(col):
    for i in range(row):
        if matrix[i][j] == num:
            print(j, end=' ')
            break
print()