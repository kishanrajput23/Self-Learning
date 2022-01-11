text = []
for i in open("C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt"):
    text.append(i)
print(text)

for i in range(len(text)):
    if text[i][-1] == '\n':
        text[i] = text[i][:-1]
print(text)