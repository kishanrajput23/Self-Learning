lines = 0
words = 0
letters = 0

fp = "C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt"

for line in open(fp):
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
print("Lines: ",lines)
print("Words: ",words)
print("Letters: ",letters)