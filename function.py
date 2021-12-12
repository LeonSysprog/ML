def change_lst(lst):
    n = len(lst)
    for i in range(0, n):
        if lst[i] % 2 == 1:
            lst[i] += 10
            
lst = [1, 3, 4, 5, 7]
change_lst(lst)
print(*lst)
