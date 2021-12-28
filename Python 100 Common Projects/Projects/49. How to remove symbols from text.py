str = input("Insert some text with punctuation marks: \n")
symbols = ['.',',',':',';','!','?','(',')']

listitem = str.split()

x = 0
for i in listitem:
    if i[-1] in symbols:
        listitem[x] = i[:-1]
        i = listitem[x]
    if i[0] in symbols:
        listitem[x] = i[1:]
    x += 1

x = 0
while x < len(listitem):
    print(listitem[x], end=' ')
    x += 1
    if x%5 == 0:
        print()