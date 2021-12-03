str  = input("Insert a string: ")
len_str = len(str)

for i in range(len_str//2):
    if str[i] != str[-1-i]:
        print("This is NOT a palindrome!")
        quit()
print("This is a PALINDROME!")