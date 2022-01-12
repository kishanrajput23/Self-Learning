x = ['a','b','c','d','e']
y = input("Insert a letter: ")

if y in x:
    print(1)
else:
    raise ValueError("Letter does not exist!")
