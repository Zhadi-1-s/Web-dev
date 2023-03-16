l = []

n = int(input())

for i in range(1,n):
    if n%i == 0:
        l.append(i)

print(l)

st = 0
end = len(l)-1

while end >= st:
    mid = (st + end) // 2
    if n / l[mid] == l[mid]:
        print("Yes")
        break
    elif n / l[mid] > l[mid]:
        st = mid + 1
    else:
        end = mid - 1

