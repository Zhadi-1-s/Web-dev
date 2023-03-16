from pydoc import describe


nums = list(map(int , input().split()))

dec = {}

for i in nums:
    if i not in dec:
        dec[i] = 1
    else:
        dec[i]+=1

sum = 0


for i in nums:
    if dec[i] > 1:
        continue
    else:
        sum+=i
print(sum)