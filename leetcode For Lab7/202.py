n = int(input())

l = [] 

sum = 0

while n not in l:
    l.append(n)
    for i in str(n):
        sum += int(i)**2
    if sum == 1:
        print("Yes")
        break
    else:
        n = sum
    