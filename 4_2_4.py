n = (int)(input())
d = dict([])
ans = []

for i in range(0, n):
    record = input()
    ans.append(record)
    lst = [str(x) for x in record.split()]
    d[record] = (lst[0], lst[3]);
    
# Insertion sort 
length = len(ans)

for index in range(1, length):
    x = ans[index]
    j = index
    while (j > 0 and (d[ans[j-1]])[0] > (d[x])[0] or ((d[ans[j-1]])[0] == (d[x])[0] and (d[ans[j-1]])[1] > (d[x])[1])):
        ans[j] = ans[j-1]
        j -= 1
    ans[j] = x

for rec in ans:            
    print(rec)
