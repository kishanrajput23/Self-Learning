n = int(input())
symbol = input();
vowels = 'aeiouAEIOU'
list1 = []

for i in range(n):
    str1 = input()
    list1.append(str1)
    
result = []
countt_list = []

for j in list1:
    for k in j:
        if k in vowels:
            j = j.replace(k, symbol)
    result.append(j)
    
for i in result:
    count = 0
    for j in i:
        if j == symbol:
            count +=1
    countt_list.append(count)
  
for l in range(len(result)):
    print(result[l] + str(countt_list[l]))
