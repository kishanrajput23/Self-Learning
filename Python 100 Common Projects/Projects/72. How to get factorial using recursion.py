def factorial(x):
    if x == 1:
        return x
    return x * factorial(x-1)
y = int(input("Insert any number to calculate factorial: "))
print(factorial(y))