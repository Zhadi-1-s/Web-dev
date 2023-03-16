s = input()

dic = {}
x = ""
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] +=1

for i in dic:
    maxim = max(list(dic.values()))
    if dic[i] == maxim:
        for i in range(maxim):
            maxim+=i
        dic.pop(i,maxim)
print(x)