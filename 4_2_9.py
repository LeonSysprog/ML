n = (int)(input())
matrix = []
for i in range(0, n):
    record = input()
    lst = [int(x) for x in record.split()]
    for dig in lst:
        matrix.append(dig)
    
# Insertion sort - 2 TL in contest

for i in range(1, n * n):
    x = matrix[i]
    j = i
    
    while (j > 0 and matrix[j - 1] > x):
        matrix[j] = matrix[j - 1]
        j -= 1
        
    matrix[j] = x

print("#")

count = 0
for i in range(0, n):
    for j in range(count, n + count):
        print(matrix[j], end= ' ')
    print()
    count += n
