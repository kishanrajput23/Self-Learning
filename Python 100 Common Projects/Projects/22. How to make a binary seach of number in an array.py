from random import random
N = 20
array = []
for x in range(N):
    array.append(int(random()*100))

array.sort()
print(array)

number = int(input("Search for any number in the array: "))

mini = 0
maxi = N-1

while mini <= maxi:
    mid = (mini + maxi) // 2
    if number < array[mid]:
        maxi = mid-1
    elif number > array[mid]:
        mini = mid+1
    else:
        print("The number is located at index: ", mid)
        break
else:
    print("There is no number!")
