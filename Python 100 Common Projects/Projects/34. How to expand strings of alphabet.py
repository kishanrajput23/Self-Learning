str1 = input("Insert starting letter: ")
str2 = input("Insert ending letter: ")

while str1 <= str2:
    print(str1, end=" ")
    str1 = chr(ord(str1) + 1)
print()
