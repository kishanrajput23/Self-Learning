str = input("Insert different strings: ")
first = str.split()
len_first = len(first)

for i in range(len_first - 1):
    for j in range(len_first - 1 -i):
        if len(first[j]) > len(first[j + 1]):
            first[j], first[j + 1] = first[j + 1],first[j]
print(' '.join(first))