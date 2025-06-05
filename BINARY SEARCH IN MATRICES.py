#search a element in the given matrix
a= 		[[10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]]
element = 50
f= False
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == element:
            print(f"Element {element} found at position ({i}, {j})")
            f= True
            break  
    if f:
        break
if not f:
    print(f"Element {element} not found in the matrix.")
    

#Searching an element in matrix using row-wise binary search
def binary_search(a, x):
    l = 0
    h = len(a) - 1
    while l <= h:
        mid = (l + h) // 2
        if a[mid] == x:
            return 1
        elif x < a[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return 0
a = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
x =50
f=1
for i in a:
    if i[0] <= x <= i[-1]:
        if binary_search(i, x):
            print("Found")
            f=0
            break
if f==1:
    print("not found ")
    
#or
#Optimized code
def binary_search(a, x):
    n=4
    m=4
    l = 0
    r=n*m-1
    while l <=r:
        mid = (l+r) // 2
        if a[mid//m][mid%m]==x:
            return "Found"
            break
        elif x<a[mid//m][mid%m]:
            r=mid - 1
        else:
            l=mid + 1
    return "Not Found"
a = [
    [2,3,7,8],
    [9,15,20,22],
    [23,26,35,37],
    [38,39,42,43],
]
x =42
print(binary_search(a,x))

# without using Function
a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,22,25],
    [28,30,33,37]
]
target=12
n=len(a)
m=len(a[0])
l=0
r=n*m-1
found=False
while l<=r:
    mid=(l+r)//2
    if a[mid//m][mid%m]==target:
        print("Element found")
        found=True
        break
    elif a[mid//m][mid%m]<target:
        l=mid+1
    else:
        r=mid-1
if not found:
    print("Element not found.")
    
#a=[1,2,3,4,5,6,7,8,9,10] capacity is 12 print the no of days if its possible
#minimum number of days required to complete all the items
#such that the total load on any day does not exceed the capacity c.
a=[1,2,3,4,5,6,7,8,9,10]
c=12
d=1
s=0
for i in a:
    if s+i>c:
        d=d+1
        s=0
    s+=i        
print(d)
    
#Given a 2D matrix where each row and column is sorted in increasing order
#and an integer k, determine if k exists in the matrix.
a=[
    [3,4,6,8],
    [5,7,9,10],
    [8,12,13,15],
    [20,23,26,28],
    [30,36,40,45]
    ]
k=23
row=len(a)
col=len(a[0])
r=0
c=col-1
while r<row and c>=0:
    if a[r][c]==k:
        print("found")
        break
    elif a[r][c]>k:
        c-=1
    elif a[r][c]<k:
        r+=1
else:
    print("not found")
    
'''
a[2,5,7,11,15] target=26
sum of elemnts=target or not print index
'''   
a=[2,5,7,11,15]
t=26
for i in range(len(a)-1):
    for j in range(len(a)-1,i,-1):
        if a[i]+a[j]==t:
            print(i,j)
            break
    
    