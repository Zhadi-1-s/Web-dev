matrix = []

for i in range(4):
    s = list(map(int , input().split()))
    matrix.append(s)

# for i in range(0,len(matrix),len(matrix)-i):
#     for j in range(0,len(matrix[i]),len(matrix[i]-j)):

# i = j = 0
# cnt = 0
# res = []
# while cnt < len(matrix):
#     if j == 0 and i < len(matrix):
#         res.append([matrix[i][j]])
#         i+=1
#     if i == len(matrix) - 1 and j :
#         res.append()

matrix.reverse()

print(matrix)