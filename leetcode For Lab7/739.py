temp = list(map(int , input().split()))

cnt = 1

res = []

for i in range(len(temp)- 1):
    if temp[i] < temp[i+1]:
        res.append(cnt)
    else:
        cnt = 0
        for j in range(i+1,len(temp)):
            cnt+=1
            if temp[j] > temp[i]:
                res.append(cnt)
                break    
            if j == len(temp)-1:
                res.append(0)
        cnt = 1
    if i+1 == len(temp) - 1:
        res.append(0)

print(res)