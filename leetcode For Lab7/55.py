nums = list(map(int , input().split()))

i = 0

while i < len(nums):
    if nums[i] == 0:
        break
    i = i + nums[i]

if i > len(nums):
    print(True)
else:
    print(False)