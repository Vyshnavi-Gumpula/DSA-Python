'''given an array print the freq of a k value in given list
ip:[2,4,6,3,3,2,6,1,3,6,6,5]
k=6
op:4(6 occurred 4 times)'''
def k_occurance(a,i,k):
    if i==len(a):
        return 0 
    if a[i]==k:
        return 1+k_occurance(a,i+1,k)
    else:
        return k_occurance(a,i+1,k)
    
def itrate(a,f,i=0):
    if i==len(a):
        return "Not Found"
    if k_occurance(a,0,a[i])==f:
        return a[i]
    return itrate(a,f,i+1)    
#[2,4,6,3,3,2,6,1,3,6,6,5]
a=list(map(int,input().split()))
k=int(input())
f=int(input())
print(k_occurance(a,0,k))
print(itrate(a,f))



#dictionary
def value(x,f,d,i=0):
    if(i==len(x)):
        return "not found"
    if(d[x[i]]==f):
        return x[i]
    return value(x,f,d,i+1)
def freq_d(x,f,d={},i=0):
    if(i==len(x)):
        return value(list(d.keys()),f,d)
    if(x[i] not in d):
        d[x[i]]=1
    else:
        d[x[i]]+=1
    return freq_d(x,f,d,i+1)
a=[2,3,3,6,5,5,9,8,8,4,6,6]
f=3
print(freq_d(a,f))

#Print all SUBSETS
def subset(a, i=0, curr=[]):
    if i == len(a):
        print(curr)
        return
    subset(a,i+1,curr+[a[i]])
    subset(a,i+1,curr)
a = [2, 3, 4]
subset(a)

'''[1,2,4,5] and k=6 checking subsets sum=k or not '''
def check_sum(a, k, i=0):
    if k==0:
        return True
    if i == 0:
        return False
    if a[i-1]>k:
        return check_sum(a,k,i-1)
    return check_sum(a,k-a[i-1],i-1) or check_sum(a,k,i-1)
a = [1,3,2, 4, 5]
k = 25
print(check_sum(a,k,len(a)))

#Print the subsets with sum k
def sub_set(a,k,s=[],i=0):
    if i == len(a):
        if k==0:
            print(s)
        return
    if a[i]<=k:
        sub_set(a,k-a[i],s+[a[i]],i+1)
    sub_set(a,k,s,i+1)
a=[2,3,4,5]
k=9
sub_set(a,k)

'''ip:[2,4,6,8]
13 is it possible to form 13 ruppes from the coins or not if not print -1
if yes op:2(minimum no of coins req to form)'''
def sub_set(a,k,s=0,i=0,m=999999):
    if i == len(a):
        if k==0:
            if s<m:
                m=s
        return m
    if a[i]<=k:
        m=sub_set(a,k-a[i],s+1,i+1,m)
    m=sub_set(a,k,s,i+1,m)
    return m
a=[2,3,4,5]
k=9
print(sub_set(a, k))







