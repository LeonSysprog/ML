n = (int)(input())
matrix = []
for i in range(0, n):
    record = input()
    lst = [int(x) for x in record.split()]
    matrix.append(lst)
    

for i in range(0, n):
    # Insertion sort 

    for index in range(1, n):
        x = matrix[index][i]
        j = index
        while (j > 0 and matrix[j - 1][i] > x):
            matrix[j][i] = matrix[j - 1][i]
            j-=1
            
        matrix[j][i] = x

for record in matrix:
    print(*record)
