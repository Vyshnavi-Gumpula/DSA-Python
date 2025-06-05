'''
ip:[2,13,4,2,9,9,5,8,7,13,3]
print the kth largest element (k=3 & largest ele=8)
without duplicates
'''
a= [2, 3, 4, 2, 9, 9, 5, 8, 7, 13, 3]
k = 3
b=[0 for i in range(max(a)+1)]
print(b)
for i in a:
    b[i]=1
for i in range(len(b)-1,-1,-1):
    if (b[i]==1):
        k=k-1
    if k==0:
        print(i)
        break
    
    
'''ip:[2,13,4,2,9,9,5,8,7,13,3]
kth largest element with duplicates
'''
a=[2,13,4,2,9,9,5,8,7,13,3]
k=3
b=[0 for i in range(max(a)+1)]
print(b)
for i in a:
    b[i]+=1
for i in range(len(b)-1,-1,-1):
    if b[i]!=1:
        k=k-b[i]
    if k<=0:
        print(i)
        break

'''print the element with highest frequency'''
a=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=0
for i in d:
    if d[i]>m:
        m=d[i]
        res=i
print("value with highest freq:",res)

'''kth largest freq'''
a=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
d={}
k=3
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
m=max(d.values())
b=[0 for i in range(m+1)]
for i in d:
        b[d[i]]=max(b[d[i]],i)        
print(b)
print(b[-k])

'''
ip:[7,2,6,3,6,7,7,2,2,2]
sort them according to their frequency
'''
a = [7, 2, 6, 3, 6, 7, 7,7, 2, 2]
f= {}
for x in a:
    if x in f:
        f[x] += 1
    else:
        f[x] = 1
u = list(f.keys())
for i in range(len(u)-1):
    for j in range(len(u)-1-i):
        if f[u[j]] > f[u[j+1]]:
            u[j], u[j+1] = u[j+1], u[j]

print(u)
