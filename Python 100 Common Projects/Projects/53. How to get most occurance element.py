from random import random

x = [int(random()*100)for i in range(20)]
print(x)

myset = set(x)

highest = None
frequent = 0

for item in myset:
    freq = x.count(item)

    if freq > frequent:
        frequent = freq
        highest = item
print(highest)