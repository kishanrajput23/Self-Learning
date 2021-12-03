str = input("Insert some strings: ")
totalstr = str.split()

longest = 0

for i in range(1, len(totalstr)):
    if len(totalstr[longest]) < len(totalstr[i]):
        longest = i
print(totalstr[longest])