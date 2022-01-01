def fibonacci(list_item):
    f1 = f2 = 1
    print(f1, f2, end=' ')
    while list_item > 2:
        num = f2
        f2 = f1 + f2
        f1 = num
        print(f2, end=' ')
        list_item -= 1
    print()

x = int(input("Insert range of Fibonacci sequence: "))
fibonacci(x)