#even or odd in 4 methods
#method-1
n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")
#method-2
if n&1==1:
    print("odd")
else:
    print("even")
#method-3   
if n^1==(n+1):
    print("even")
else:
    print("odd")
#method-4    
if n^(n-1)==1:
    print("odd")
else:
    print("even")
#Sum of n numbers
#Tym complexity=O(n)
n=int(input())
sum=0
for i in range(n+1):
    sum+=i
print(sum)
#Tym Complexity=O(1)
print(n*(n+1)/2)
#PERFORMING XOR:
#(QUESTION)INPUT:5-----------OUTPUT: 1^2^3^4^5
'''Tym Complexity=O(n)'''
n=int(input())
s=0
for i in range(1,n+1):
    s=s^i
print(s)
'''Tym Complexity=O(1)''' 
if n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)
else:
    print(n)
#xor from n to m
def xor_upto(n):
    if n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n+1
    elif n % 4 == 3:
        return 0
    else:
        return n
n,m= map(int, input().split())
result = xor_upto(m) ^xor_upto(n - 1)
print(result)

s=0
for i in range(5,11):
    s=s^i
print(s)
print()
#(WHETHER A NUMBER IS POWER OF 2 OR  NOT)
#TIME COMPLEXITY=O(1)
n = int(input())
if (n & (n - 1)) == 0:
    print("Yes")
else:
    print("No")
#OR-----(O(logn))
while n%2==0:
    n=n//2
if n==1:
    print("yes")
else:
    print("No")
#Return the Single frequency value
li=[2,3,4,3,2,5,5]
d={}
for c in li:
    if c not in d:
        d[c]=1
    else:
        d[c]+=1
for k,v in dict.items(d):
    if v<2:
        print(k)

#OR
s=0
for i in li:
    s=s^i
print(s)
#Prime ir not in given range
n=int(input())
for i in range(2, int(n*(0.5))):  
        if n % i == 0:
            print(" not prime number")
            break
else:
    if n<200:
        print("prime number is less than 200")
    else:
        print("prime number is greater than 200")
#Remove duplicates
def remove_duplicates(seq):
    ul = []
    for x in seq:
        if x not in ul:
            ul.append(x)
    return ul
i = [8, 2, 3, 4, 3, 3, 4, 5, 6, 7, 9, 2, 4]
print(remove_duplicates(i))
