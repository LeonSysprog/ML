n = (int)(input())

for i in range(0, n):
    record = input()
    lst = [int(x) for x in record.split()]
    
    # Bubble sort 
    length = len(lst)

    for index in range(0, length):
        for index2 in range(0, length):
            if (lst[index] > lst[index2]):
                lst[index], lst[index2] = lst[index2], lst[index]
        
    print(*lst)
