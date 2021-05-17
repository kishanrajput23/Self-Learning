x = abs(int(input("Insert integer values only: ")))

sum = 0
mul = 1

while x != 0:
    digit = x%10
    sum += digit
    mul *= digit

    x = x/10

print("Sum of digit = ",sum)
print("Product of digit = ",mul)