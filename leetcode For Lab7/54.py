n = int(input())

m = int(input())

matrix = []

for i in range(n):
    s = list(map(int , input().split()))
    matrix.append(s)

i , down = 0,len(matrix)-1
j , left = 0,len(matrix[0])-1
res = []
while i <= down and j <= left:
    if i == 0 and j <= left:
        res.append(matrix[i][j])
        j+=1
    if j == left and i <= down:
        i+=1
        res.append(matrix[i][j])
    if i == down and j <= left:
        j-=1
        res.append(matrix[i][j])
