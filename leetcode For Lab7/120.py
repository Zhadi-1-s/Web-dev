matrix = [[2],[3,4],[6,5,7],[4,1,8,3]]

cnt = 0


for i in range(1,len(matrix)):
    for j in range(len(matrix[i])):
        if j == 0:
            matrix[i][j]+=matrix[i-1][j]
            j = matrix[i].index(min(matrix[i][j],matrix[i][j+1]))
        elif j == len(matrix[i]) - 1:
            matrix[i][j]+= matrix[i-1][j-1]
        else:
            matrix[i][j]+=min(matrix[i-1][j-1],matrix[i-1][j])

print(min(matrix[-1]))