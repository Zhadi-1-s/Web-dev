nums = list(map(int , input().split()))
nums.sort()
dic = {}

for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1

print(dic)
print(nums)