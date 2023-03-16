nums = list(map(int , input().split()))

for i in range(len(nums),0,-1):
    if nums[i] < 0 and nums[i-1] > 0:
        
