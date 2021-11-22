matrix = [[1,2,3],[4,5,6],[7,8,9]]

def transpose_matrix(matrix):
    transpose=[[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transpose[j][i]=matrix[i][j]
    return transpose
        
print(transpose_matrix(matrix))