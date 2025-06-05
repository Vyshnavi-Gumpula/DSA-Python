#BUBBLE SORT
def sort(n):
     for i in range(len(n)):
         for j in range(len(n)-i-1):
             if n[j]>n[j+1]:
                 n[j],n[j+1]=n[j+1],n[j]
     return n
n=list(map(int,input().split()))
print(sort(n))

#bubble sort using sliding window
#MOST EFFICIENT WAY
#a=[3,5,1,2,4,7,9,3]
a= list(map(int,input().split()))
c=0#comparision count
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        c=c+1
        if a[i]>a[i+1]:
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)
print("Comparision",c)

#or
a=[5,2,3,9,10,1]
for _ in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a)


'''ip:[5,2,3,8,1,6,7]
  if k=2 dont sort first k elements and last k elements'''
a=[5,2,3,8,1,6,7]
k=2
for j in range(len(a)-2*k-1):
    f=False
    for i in range(k,len(a)-1-k-j):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            f=True
    if f==False:
        break
print(a)

'''a=[2,5,8,6,3,1,9,4,7]
k=4
print Kth largest element using bubble sort'''
a=list(map(int, input().split()))
k=int(input())
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            f= True
    if f==False:        
        break
print(a)
print(a[-k])

#or
a=list(map(int, input().split()))
k=int(input())
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            f= True
    k=k-1
    if f==False or k==0:        
        break
print(a)
print(a[-k])

'''ip:['c','e','a','b','f']
  op:[a,b,c,e,f] sort according to the asci values"
  '''
a = ['c', 'e', 'b','d', 'f','a']
for _ in range(len(a) - 1):
    for i in range(len(a) - 1): 
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)
#or
a=['c', 'e', 'b','d', 'f','a']
c=0#comparision count
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        c=c+1
        if ord(a[i])>ord(a[i+1]):
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)
print(c)

'''sort according to the 2nd element
ip:[[2,3],[5,1],[1,4],[2,7],[1,3]]
op:[[5,1],[2,3],[1,3],[1,4],[2,7]] '''
a = [[2, 3], [5, 10], [1, 4], [2, 7], [1, 3]]
for _ in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i][1] > a[i + 1][1]:
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)

#or
a = [[2, 3], [5, 10], [1, 4], [2, 7], [1, 3]]
c=0#comparision count
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        c=c+1
        if a[i][1] > a[i + 1][1]:
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)
print(c)

#or
def qwe(x):
    return x[1]
a=[[2, 3],[5, 1],[1, 4],[2, 7],[1, 3]]
a.sort(key=qwe)
print(a)

'''#sort the strings in a list in lexographical order compare only two charcters.
if first 2 characters are same dont sort
   ip:["zebra","cat","car","apple"]
   op:["apple","cat","car","zebra"] 
'''
a=["zebra","car","cat","apple","hat","happy"]
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1):
        if a[i][:2]!=a[i+1][:2] and a[i]>a[i+1]:
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)
#or
a = ['zebra', 'cat', 'apple', 'car']
for i in range(len(a) - 1):  
    f = False
    for j in range(len(a) - 1 - i):
        if a[j][0] > a[j + 1][0]:
            a[j], a[j + 1] = a[j + 1], a[j]
            f = True
        elif a[j][0] == a[j + 1][0] and a[j][1] > a[j + 1][1]: 
            a[j], a[j + 1] = a[j + 1], a[j]
            f = True
    if f == False:
        break
print(a)
''' given a 2d list in every list there is a prime no
sort the list according to the prime nos
ip:[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
op:[[14,8,3],[8,10,5],[7,9,20],[4,13,12]]
'''
a = [[4, 13, 12], [8, 10, 5], [7, 9, 20], [14, 8, 3]]
primes = []
for sublist in a:
    for num in sublist:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
                break
for j in range(len(a) - 1):
    for i in range(len(a) - 1 - j):
        if primes[i] > primes[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            primes[i], primes[i + 1] = primes[i + 1], primes[i]
print(a)
#or
def prime(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            return i
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
b=[]
for i in a:
    b.append(prime(i))
for i in range(len(b)-1):
    f=0
    for j in range(len(b)-1-i):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(a)
'''using key -sort method'''

def qwe(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            return i
    return 0
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3],[10]]
a.sort(key=qwe)
print(a)

'''
sort according to the length of the words considering the spaces also in sentence
ip:"An apple a day keeps doctor away"
op:a an day away apple keeps doctor
'''
a = "An apple a day keeps doctor away".split()
b = []                
for i in a:
    b.append(len(i))
for i in range(len(b)-1):
    f = 0
    for j in range(len(b)-1-i):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f = 1
    if f == 0:
        break
res = ' '.join(a)
print(res)

'''BUCKET SORT
    ip:[7,2,2,6,3,6,7,7,2]
    op:[3,6,6,7,7,7,2,2,2]'''
a=[3,5,4,4,5,6,7,7,8,8,7,6,4,1,1,2,8,8]
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
print(b)
for i in d.items():
    b[i[1]].append(i[0])
print(b)
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)

        

        