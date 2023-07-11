def transpose2(matrix, n):
    # Write Your code here
    output = [[0] * n for i in range(n)]
    for j in range(n):
        for k in range(n):
            output[j][k] = matrix[k][j]
    return output

def transpose(matrix,n):
    output = list()
    for i in range(n):
        output.append([])
        for j in range(n):
            # replace a[i][j] with a[j][i]
            output[i].append(matrix[j][i])
    return output

m = [[1, 1, 1, 1],
[2, 2, 2, 2],
[3, 3, 3, 3],
[4, 4, 4, 4]]
print(transpose(m,4))