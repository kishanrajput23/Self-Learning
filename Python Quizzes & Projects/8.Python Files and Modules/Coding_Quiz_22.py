# Write  a Python code to read the first three lines of a file?

from itertools import islice

with open("Python.txt", "r") as file:
    data = file.readlines()
    
    for i in islice(data, 3):
        print(i)