num1 = int(input("Insert number to convert: "))
base_num = int(input("Choose the base(2-9): "))

if not(2<= base_num <=9):
    quit()

num2 = ''

while num1>0:
    num2 = str(num1%base_num) + num2
    num1 //= base_num

print(num2)