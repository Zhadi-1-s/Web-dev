n = int(input())

cnt = 1
res = []

for i in range(n):
    res.append(1)

i = len(res)-1

while len(res) > 1:
    res[i-1] += res[i]
    res.pop(i)
    i-=1
    cnt+=1

print(cnt)