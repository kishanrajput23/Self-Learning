num = int(input("Enter the number "))

sum = 0
i = 0
while i < num+1:
    sum += i
    i += 1

print("The sum of first " + str(num) + " natural numbers are", sum)