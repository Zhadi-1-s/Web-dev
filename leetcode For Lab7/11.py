height = list(map(int , input().split()))

i = 0
j = len(height) - 1

maxArea = 0

while i < j:
    x = (j-i) * min(height[i],height[j])
    if maxArea < x:
        maxArea = x
    