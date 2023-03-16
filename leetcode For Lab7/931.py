matrix = [[2,1,3],[6,5,4],[7,8,9]]

j = min(matrix[0])

cnt = j

index = matrix[0].index(j)

minimum = -100000

# while index <= len(matrix):
#     if index < len(matrix[0]):
#         for i in range(1,len(matrix)):
#             for j in range(index - 1,index + 2):
#                 if minimum < matrix[i][j]:
#                     minimum = matrix[i][j]
#                     cnt+=minimum

i = 0

while i <= len(matrix):
    if index < len(matrix[0]):
        for k in range(1,len(matrix)):
            for l in range(index -1,len(matrix[0] - index + 1)):
                if minimum < matrix[k][j]:
                    minimum = matrix[k][j]
                    cnt+=minimum
                    i+=1
                    index = matrix[k].index(minimum)
