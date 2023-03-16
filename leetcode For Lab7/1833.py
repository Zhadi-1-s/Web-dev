costs = list(map(int , input().split()))

coins = int(input())



sum = 0
cnt = 0
for i in costs:
    if i <= coins:
        cnt+=1
        coins -= i
    else:
        break
print(cnt)
