l = []

for i in range(3):
    s = list(map(int , input().split()))
    l.append(s)

counter = 0

flag = False

res = []

for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == 0:
            res.append([i,j])

for i in res:
    for k in range(len(l)):
        for j in range(len(l[k])):
            l[i[0]][j] = 0
        l[k][i[1]] = 0 

print(l)
