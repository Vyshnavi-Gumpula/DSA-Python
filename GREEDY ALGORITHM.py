#greedy algorithm
#print largest even and smallest odd
def leso(a):
    le,so=0,0
    for i in a:
        if i%2==0:
            if le==0 or i>le:
                le=i
        else:
            if so==0 or i<so:
                so=i
    return le,so
a=list(map(int,input().split()))
print(leso(a))
#or
a=list(map(int,input().split()))
m=0
m1=999999
for i in a:
    if(i>m and i%2==0):
        m=i
    if (i<m1 and i%2!=0):
        m1=i
print(m,m1)


#Print Second Maximum 
a=[4,5,6,7,8,13,9,11]
m=0
m1=0
for i in a:
    if i>m:
        m1=m
        m=i
    elif i >m1 and i != m:
        m1= i
print(m1)

'''ip:[13,14,2,5,8,1,4]
        m,t,w,th,f,sa,su
maximum profit'''
#Tym Complexity=O(n)(Greedy)
a=[13,14,2,5,8,1,4]
profit=0
buy=a[0]
for i in range(1,len(a)):
    if a[i]>buy:
        if a[i]-buy>profit:
            profit=a[i]-buy
    else:
        buy=a[i]
print(profit)
#Two pointer approach:O(n*n)
a=[13,14,2,5,8,1,4]
mp=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>mp:
            mp=a[j]-a[i]
print(mp)




