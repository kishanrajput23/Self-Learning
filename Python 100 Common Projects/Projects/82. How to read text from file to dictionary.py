goods = {}

for i in open("C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt"):
    cate = i.split()
    cate[1] = float(cate[1])
    cate[2] = int(cate[2])
    goods[cate[0]] = cate[1:]
print(goods)