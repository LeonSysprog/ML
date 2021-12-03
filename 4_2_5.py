n = (int)(input())
d = dict([])
ans = []

for i in range(0, n):
    record = input()
    ans.append(record)
    lst = [str(x) for x in record.split()]
    d[record] = (lst[0], lst[3]);
    
# Selection sort 
length = len(ans)

for index in range(0, length):
    j = index
    for index2 in range(index + 1, length):
        if ((d[ans[index2]])[0] < (d[ans[j]])[0] or ((d[ans[index2]])[0] == (d[ans[j]])[0] and (d[ans[index2]])[1] > (d[ans[j]])[1])):
            j = index2
    ans[index], ans[j] = ans[j], ans[index]

for rec in ans:            
    print(rec)
