from random import randint
col = 6
row = 3
matrix = []
for i in range(row):
    myrow = []
    for j in range(col):
        myrow.append(randint(10,100))
    matrix.append(myrow)
for i in matrix:
    print(i)
print()
k = col-1
while k != 0:
    z = 0
    for j in range(1, k+1):
        if matrix[0][j] > matrix[0][z]:
            z = j
    for i in range(row):
        y = matrix[i][z]
        matrix[i][z] = matrix[i][k]
        matrix[i][k] = y
    k -= 1
for i in matrix:
    print(i)