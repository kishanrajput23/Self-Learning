f = open('sample.txt')
# read first line
data = f.readline() 
print(data)

# Read second line
data = f.readline() 
print(data)

# Read third line
data = f.readline() 
print(data)

# Read fourth line... and so on...
data = f.readline() 
print(data)
f.close()