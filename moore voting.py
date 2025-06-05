'''
ip:[2,1,1,2,3,1,1]
find the no which frq is > half of the list
'''
a=[2, 1, 1, 2, 3, 1, 1]
n=(len(a))/2
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
for i in d:
    if d[i]>n:
        print(i)
        break

#Boyer-Moore Voting Algorithm
a = [2, 1, 1, 2, 3, 1, 1]
res = a[0]
count = 1
for i in range(1,len(a)):
    if res==a[i]:
        count += 1
    else:
        count -= 1
        if count==0:
            res=a[i]
            count=1
print(res)
