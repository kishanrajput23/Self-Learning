x = abs(int(input("Insert range of sequence: ")))

f1 = f2 = 1
print(f1,f2,end=" ")

for y in range(x-2):
    print(f1+f2, end=" ")
    f1, f2 = f2, f1+f2