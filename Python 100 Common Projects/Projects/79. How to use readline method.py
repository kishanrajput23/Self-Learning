fp = open("C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt")
data = []

i = fp.readline()
while i != '':
    data.append(i)
    i = fp.readline()
fp.close()
print(data)