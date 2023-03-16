nums = list(map(int , input().split()))

k = int(input())

dic = {}

for i,j in enumerate(nums):
    if j in dic and abs(i - dic[j]) <=k:
        print(True)
    else:
        dic[j] = i

print(dic)