n = (int)(input())
d = dict([])
ans = []
for i in range(0, n):
    record = input()
    ans.append(record)
    lst = [str(x) for x in record.split()]
    averageMark = (float(lst[4]) + float(lst[5]) + float(lst[6]) + float(lst[7]) + float(lst[8])) / 5
    d[record] = averageMark;
    
# Bubble sort 
length = len(ans)

for index1 in range(0, length):
    for index2 in range(0, length):
        if (d[ans[index1]] < d[ans[index2]]):
            ans[index1], ans[index2] = ans[index2], ans[index1]

for rec in ans:            
    print(rec)
