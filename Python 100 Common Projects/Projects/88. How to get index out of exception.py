x = [1,2,3,4,5,6,7,8,9]

print("t = terminate")

while True:
    num = input("Choose index to search: ")
    if num == 't':
        break
    try:
        num = int(num)
        print(x[num])
    except ValueError:
        print("Only integers are allowed!")
    except IndexError:
        print("Error! Number out of index", num)
