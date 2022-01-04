from random import randint

def num_search(first,last):
    mid = len(first) //2
    mini = 0
    maxi = len(first) - 1
    while first[mid] != last and mini <= maxi:
        if last > first[mid]:
            mini = mid + 1
        else:
            maxi = mid -1
        mid = (mini + maxi) // 2
    if mini > maxi:
        return None
    else:
        return mid

x = []
for i in range(15):
    x.append(randint(1,20))
x.sort()
print(x)

num = int(input("Insert any number to search the list: "))
print(num_search(x,num))