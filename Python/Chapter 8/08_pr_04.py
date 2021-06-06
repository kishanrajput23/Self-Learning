# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def sum_of_natural_nos(n):
    if n == 0:
        return n
    else:
        return n + sum_of_natural_nos(n-1)
    

print(sum_of_natural_nos(10))