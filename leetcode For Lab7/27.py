nums = list(map(int , input().split()))

val = int(input())

cnt = 0

while val in nums:
    nums.pop(nums.index(val))
    cnt+=1

