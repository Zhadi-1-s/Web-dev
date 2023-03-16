nums = list(map(int ,input().split()))
k = int(input())
dic = {}

res = []
x = 0

l = []

for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] +=1

i = 0

for i in dic.values():
    l.append(i)
while i < k:
    x = max(l)
    for j in dic:
        if dic[j] == x:
            res.append(j)
            l.pop(l.index(x))
    i+=1
print(res)