nums = list(map(int , input().split()))

dic = {0:1}

nums.sort()

cnt = 0

for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1
i = nums.index(max(nums))
while True:
    x = nums.index(max(nums))
    if nums[::-1] == nums[::1]:
        break
    else:
        i = x - dic[nums[i]]
        nums[x] = nums[i]
        cnt+=1

print(cnt)