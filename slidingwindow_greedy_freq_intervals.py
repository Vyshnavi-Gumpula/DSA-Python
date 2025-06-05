'''
ip:'abcedacefaebg'
find the length of longest non repeating substring it should contain
m='c'
n='d'
'''
#s="abcedacefaebg"
s="abcedachfaebghd"
u="c"
v="d"
m=0
d={}
l=0
start=0
for r in range(len(s)):
    if s[r] not in d:
         d[s[r]]=r
    else:
        if d[s[r]]>=l:
            l=d[s[r]]+1    
        d[s[r]]=r
    if r-l+1>m and u in d and v in d and d[u]>=l and d[v]>=l:
        m=r-l+1
        start=l
print(m)
print(s[start:start+m]) 
            
'''
[4,2,7,20,8,6,4,1]
k=3
removing the k cards from the deck of list to make maximum profit
it can be removed from either front or back and also print the cards
'''
a=[4,3,2,5,6,1,12,3]
n=len(a)
k=4
ls=0
for i in range(k):
    ls+=a[i]
rs=0
m=ls
print(ls)
for i in range(k-1,-1,-1):
    ls=ls-a[i]
    rs=rs+a[n-1]
    m=max(m,ls+rs)
    n=n-1
    print(ls,rs)
print(m)
'''
ip:[1,1,1,0,0,0,1,1,1,1,0]
k=2
'''
nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
l=0
m=0
zc=0
for r in range(len(nums)):
    if nums[r]==0:
        zc+=1
    if zc>k:
        if nums[l]==0:
            zc-=1
        l+=1
    if zc<=k:
        m=max(m,r-l+1)
print(m)
'''
ip1:[900,945,1110,1230,1235,1245,1340,1700] starting tym
ip2:[930,1130,1120,1245,1250,1415,1400,1730] ending tym
   patients booked the appointments
   print maximum no of doctors req to treat everyone
   op:2
'''
s=[900,945,1110,1230,1235,1245,1340,1700] 
e=[930,1130,1120,1245,1250,1415,1400,1730]
i=0
j=1
c=1
while i<len(s) and j<len(e):
    if e[i]>s[j]:
        c+=1
    else:
        i+=1
    j+=1
print(c)
        