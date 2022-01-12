fp = input("Enter file path: ")

try:
    file = open(fp)
except FileNotFoundError:
    print("Error! This file path does not exist...")
else:
    print(file.read())