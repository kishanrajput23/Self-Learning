fp = open("C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt")
data = fp.read()
fp.close()

print(repr(data))

data = data.split('\n')
print(data)