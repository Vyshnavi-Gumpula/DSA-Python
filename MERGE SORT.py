'''
ip1:[2,4,5,8,9]
ip2:[3,5,6,9,11,12,13]
op:[2,3,4,5,5,6,8,9,9,11,12,13]
2 sorted list merge to single sorted'''
a = [2, 4, 5, 8, 9]
b = [3, 5, 6, 9, 11, 12, 13,15]
c=[]
i,j=0,0
while(i<len(a) and j<len(b)):
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
while j<len(b):
    c.append(b[j])
    j+=1
while i<len(a):
    c.append(a[i])
    i+=1
print(c)

'''
[5,3,1,7,2]
merge sort
'''
def merge_sort(a):
    if len(a) == 1:
        return a
    m = len(a) // 2
    l = merge_sort(a[:m])
    r = merge_sort(a[m:])
    return merge(l, r)
def merge(l, r):
    i, j = 0, 0
    c = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            c.append(l[i])
            i += 1
        else:
            c.append(r[j])
            j += 1
    while j < len(r):
        c.append(r[j])
        j += 1
    while i < len(l):
        c.append(l[i])
        i += 1
    return c
a = [5, 3, 1, 7, 2]
print(merge_sort(a))
