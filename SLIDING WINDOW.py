#FINDING A NUMBER WITH FREQUENCY 1 USING sliding window :
#l=list(map(int,input().split()))
l=[2,2,3,3,6,6,7,8,8,9,9]
for i in range(0,len(l)-1,2):
    if l[i]!=l[i+1]:
        print(l[i])
        break
else:
    print(l[-1])
    
#Longest increasing sequence length:
arr=[1,2,3,2,3,4,5,6,7,8,9]
maxi= 1
count= 1
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1] + 1:
        count+= 1
    else:
        if(count>maxi):
            maxi=count
        count= 1  
if count>maxi:
    maxi=count
print("Longest increasing sequence length:",maxi)

#or
li=[1,2,3,2,3,4,5,6,7,8,9]
count = 1
max_count = 1
for i in range(len(li) - 1):
    if li[i+1] - li[i] == 1:
        count+= 1
        max_count = max(max_count, count)
    else:
        count = 1  
print("Longest increasing sequence length:", max_count)

#COUNT OF EACH CHARACTER IN STRING
s=input()
result = ""
c= 1
for i in range(0, len(s)-1):
    if s[i] == s[i+1]:
        c+= 1
    else:
        result += s[i] + str(c)
        c= 1 
result += s[-1] + str(c)
print(result)





   

