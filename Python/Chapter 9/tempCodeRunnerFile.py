content = " "
i = 1
with open("log.txt") as f:
    i+=1
    while content:
        content = f.readline()
        print(content)

        if 'python' in content.lower():
            print("Yes python is present")
            print(i)
        else:
            print("No python is not present")