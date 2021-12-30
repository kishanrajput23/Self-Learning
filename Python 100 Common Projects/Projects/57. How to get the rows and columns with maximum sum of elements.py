from random import random

matrix = []

for i in range(6):
    row = []
    for j in range(6):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

rmaxi = 0
rid = 0
i = 0

for row in matrix:
    if sum(row) > rmaxi:
        rmaxi = sum(row)
        rid = i
    i += 1
print(rid, '=', rmaxi)

cmaxi = 0
cid = 0
for i in range(6):
    sumcol = 0
    for j in range(6):
        sumcol += matrix[j][i]
    if sumcol > cmaxi:
        cmaxi = sumcol
        cid = i
print(cid, '=', cmaxi)