n = (int)(input())
d = dict([])
ans = []
for i in range(0, n):
    record = input()
    ans.append(record)
    lst = [str(x) for x in record.split()]
    averageMark = (float(lst[4]) + float(lst[5]) + float(lst[6]) + float(lst[7]) + float(lst[8])) / 5
    d[record] = averageMark;
    
# Insertion sort 
length = len(ans)

for index in range(1, length):
    x = ans[index]
    j = index
    while (j > 0 and d[ans[j-1]] < d[x]):
        ans[j] = ans[j-1]
        j -= 1
    ans[j] = x
    
for rec in ans:            
    print(rec)
