n = int(input())

l = []

for i in range(n):
    s = list(map(int , input().split()))
    l.append(s)

i = 0
j = 0

res = []

cnt = 0

while i < len(l):
    for k in range(len(l)):
        res.append(l[k][j])
        if res == l[i]:
            cnt+=1
    j+=1
    res.clear()
    if j > len(l)-1:
        i+=1
        j = 0
print(cnt)