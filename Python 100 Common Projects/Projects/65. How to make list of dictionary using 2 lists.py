x = ['a','b','c','d','e']
y = [1,2,3,4,5]

z = {}

for i in range(len(x)):
 #   z[y[i]] = x[i]
 z = dict(zip(y,x))

print(z)
