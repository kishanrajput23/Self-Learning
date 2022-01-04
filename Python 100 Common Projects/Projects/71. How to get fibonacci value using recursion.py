def fibinacci(x):
    if x == 1 or x == 2:
        return 1
    return fibinacci(x-1) + fibinacci(x-2)
print(fibinacci(10))