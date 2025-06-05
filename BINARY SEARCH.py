'''
ip:[2,4,3,1,4,2,3,4,5]
search element=4
if the element is there print the index of last occurance of the array or else -1 
'''
a=[2,4,3,1,4,2,3,4,5]
s=4
l =-1
for i in range(len(a)):
    if a[i]==s:
        l=i
print(l)

#binary search
#print the last index where the element is found
arr=[2,3,5,6,7,7,8,9,10,10,10,13,15]
target=10
def binarysearch(arr,target,low,high):
    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
            
    return -1
low=0
high=len(arr)-1
res=binarysearch(arr,target,low,high)
if res!=-1:
    print('element found:',res)
else:
    print('element not found',res)
    
'''
find the search element last occurance using binary search
'''
arr = list(map(int, input().split()))
target = int(input("Enter target: "))
def last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid       
            low = mid + 1   
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result
res = last_occurrence(arr, target)
if res != -1:
    print("Last occurrence found at index:", res)
else:
    print("Element not found")

'''
a=[2,4,6,7,8,10,13,15]
x=3 x is present in a then print the index
 x is not present in a so print the index where we should insert
'''
arr=[2,4,6,7,8,10,13,15]
x=5
def find_index(arr, x):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] ==x:
            return mid 
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low
print(find_index(arr,x))

'''
find the sqroot of a no return the floor value
'''
def mySqrt(x):
    if x == 0:
        return 0
    left, right = 1, x/2
    while left <= right:
        mid = (left + right) / 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
print(mySqrt(38))

'''
given a rotated array [15,18,20,22,2,5,8,10,12,13]
find the first element index in the original array
'''
#linear search O(n)
def find_rotation_index(arr):
    m= arr[0]
    mi= 0
    for i in range(1, len(arr)):
        if arr[i] < m:
            m = arr[i]
            mi = i
    return mi
arr = [15, 18, 20, 22, 2, 5, 8, 10, 12, 13]
print(find_rotation_index(arr))

#Binary search
def find_rotation_index_binary(arr):
    low = 0
    high = len(arr) - 1    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid    
    return low
arr = [15, 18, 20, 22, 2, 5, 8, 10, 12, 13]
print(find_rotation_index_binary(arr))


#using binary search O(logn)
#find a peak element (larger than both neighbors).
# peak elements are 10 and 6 so we can print any one at one time
a=[2,3,4,6,3,2,1,5,8,10,1,4,2]
l=0
r=len(a)-1
while l<r:
    m = (l + r) // 2    
    if (m==0 or a[m]>a[m-1] and  m==len(a) or a[m]>a[m+1] or a[m]>a[m+1]):
        print(a[m])
        break
    if(a[m+1]>a[m]):
        l=m+1
    else:
        r=m-1
#or
#find a peak element (larger than both neighbors).
def find_peak_binary(arr):
    l= 1
    h= len(arr)-1 
    while l<= h:
        mid = (l+ h) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid] 
        elif arr[mid] < arr[mid - 1]:
            h = mid - 1 
        else:
            l= mid +1 
    return -1  
a = [2, 3, 4, 6, 3, 2, 1, 5, 8, 10, 1, 4, 2]
print(find_peak_binary(a))