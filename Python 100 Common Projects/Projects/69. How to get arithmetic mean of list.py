def avg_list(first):
    last = len(first)
    sum = 0
    for i in first:
        sum += i
    return sum/last

x = input("Insert some integer values: ")
x = x.split()
for i in range(len(x)):
    x[i] = int(x[i])

average = avg_list(x)

print("The result of the average =",round(average,2))