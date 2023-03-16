nums = list(map(int ,input().split()))

n = len(nums)

dic = {}

for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1

for i in dic:
    if dic[i] > n//3:
        print(list(i))