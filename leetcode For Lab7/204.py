n = int(input())

res = [1] * n

res[0] = 0
res[1] = 0

for i in range(2,int(n**0.5) + 1):
    if res[i] != 0:
        res[i*i:n:i] = [0] * ((n-1 - i*i)//i+1)

print(sum(res))