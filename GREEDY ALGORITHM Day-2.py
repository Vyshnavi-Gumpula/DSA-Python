'''
ip:[2,2,1,0,1,3,0] = not possible
ip:[2,3,1,0,1,3,0] = possible
ip:[2,3,1,0,1,3,1] = possible
represents the levels of petrol by travelling another unit it reduces 1 and it can exchange 
'''
a = [2,2,1,0,1,3,0]
p = a[0]
for i in range(1, len(a)):
    p = p - 1
    if p < 0:
        print("Not Possible")
        break
    if a[i] > p:
        p = a[i]
else:
    print("Possible")

    
'''
ip:[5,10,5,10,10,20]=false
ip:[5,5,5,10,20]=true
ip:[5,5,10,20]=true
5rs for each lemonade
'''    
a = [5,5,5,10,20]
five=0
ten=0
for bill in a:
    if bill== 5:
        five+= 1
    elif bill== 10:
        if five== 0:
            print("False")
            break
        else:
            five-= 1
            ten+= 1
    else: 
        if ten> 0 and five>0:
            ten-=1
            five-=1
        elif five>=3:
            five-=3
        else:
            print("False")
            break
else:
    print("True")

'''
ip:[4,3,7,1,6,2]
the avg waitaing tym should be minimum
'''
a=[4,3,7,1,6,2]
a.sort()
s=0
total=0
for i in range(len(a)-1):
    s+=a[i]
    total+=s
    print(s)
print(total/(len(a)-1))

'''
ppl:[1,6,2,3,4,5]
bundle:[4,2,3,1,1,2]
ppl are asking that amount of bundle they can get equal or greater than that bundle but not less
maximum satisfied people=4
'''
p=[1,6,2,3,4,5]
b=[4,2,3,1,1,2]
p.sort()
b.sort()
i = j = count = 0
while i < len(p) and j < len(b):
    if b[j] >= p[i]:
        count += 1 
        i += 1
        j += 1
    else:
        j += 1 

print("Maximum satisfied people =", count)

'''
ip:[2,3,1,4]=true
ip:[2,1,1,0,3]=false
reach the last by jumping
'''
nums=[2,1,1,0,3]
goal=len(nums)-1
for i in range(len(nums)-2,-1,-1):
    if nums[i]+i>=goal:
        goal=i
if goal==0:
    print("True")
else:
    print("False")
    

'''ip:[2,3,1,1,4]
we can reach the last but print minimum no of jumps 
'''
a= [2, 3, 1, 1, 4]
l=0
r=0
jump=0
f=0
while r<len(a)-1:
    m=0
    for i in range(l,r+1):
        if i+a[i]>m:
            m=i+a[i]
        if m>len(a)-1:
            f=1
    l=r+1
    r=m
    jump+=1
print('min no of jumps',jump)

