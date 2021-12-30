from random import randint

col = 6
row = 6
matrix = []

sum_col = [0]*col
sum_row = [0]*row

for i in range(row):
    myrow = []
    for j in range(col):
        myrow.append(randint(0,3))
    matrix.append(myrow)

for i in range(row):
    for j in range(col):
        sum_row[i] += matrix[i][j]
        sum_col[j] += matrix[i][j]

for i in range(row):
    print(matrix[i], "|", sum_row[i])

print("_" *col*4)
print(sum_col)