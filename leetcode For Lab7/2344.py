import math

nums = list(map(int , input().split()))
numsDivide = list(map(int , input().split()))

g = math.gcd(*numsDivide)

for i,j in enumerate(nums):
    if g%j == 0:
        print(i)
    if j > g:
        print(-1)
        break
