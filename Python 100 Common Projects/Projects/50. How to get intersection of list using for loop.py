x = [6,8,9,10,[3,6,4],'t','tt','u',5]
y = [8,19,6,[3,6,4],'tt','u','z']
z = []

for i in x:
    for j in y:
        if i == j:
            z.append(i)
            break
print(z)