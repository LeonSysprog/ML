n = (int)(input())
matrix = []
for i in range(0, n):
    record = input()
    lst = [int(x) for x in record.split()]
    matrix.append(lst)
    
# Selection sort
for i in range(1, n-1):
    j = 0
    while (j < n and j + i < n):
        m1 = j
        m2 = j
        y = j + 1 
        while (y < n and y + i < n):
            if (matrix[m1][i + m1] < matrix[y][y + i]):
                m1 = y
            if (matrix[m2 + i][m2] > matrix[y + i][y]):
                m2 = y
            y += 1
                
        matrix[j][i + j], matrix[m1][i + m1] = matrix[m1][i + m1], matrix[j][i + j]
        matrix[j + i][j], matrix[m2 + i][m2] = matrix[m2 + i][m2], matrix[j + i][j]
        j += 1
    
for record in matrix:
    print(*record)
