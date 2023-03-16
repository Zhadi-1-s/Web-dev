nums = list(map(int , input().split()))

indexDiff = int(input())

valueDiff = int(input())

dic = {}

for i ,j in enumerate(nums):
    if j in dic and abs(i - dic[j]) <= indexDiff and i != dic[j] and abs(nums[i] - nums[dic[j]]) <= valueDiff:
        print(True)
    else:
        dic[j] = i

        