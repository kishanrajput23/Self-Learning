n = 3

for i in range(3):
    for j in range(3):
        if i == 0 or i == 3-1 or j == 0 or j == 3-1:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()