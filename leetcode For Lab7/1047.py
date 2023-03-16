s = input()

dic = {}

for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] +=1

l = list(s)

res = ""

for i in l:
    if dic[i] > 1:
        if dic[i] % 2 == 0:
            l.pop(l.index(i))
            dic[i] -=1
    else:
        res+=i

print(dic)