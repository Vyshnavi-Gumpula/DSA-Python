'''
ip:m1=[0,3,8,1,5,7,9] starting tym of meeting
   m2=[5,6,10,2,6,9,11] ending tym of meeting
maximum no of meetings conducted is 3
'''
s=[0,3,8,1,5,7,9]
e=[5,6,10,2,6,9,11]
meetings = list(zip(s,e))
meetings.sort(key=lambda x: x[1])
print(meetings)
count=0
end=0
for i,j in meetings:
    if i>end:
        count+=1
        end=j
print(count)

start=0
count=0
for i in meetings:
    if i[0]>=start:
        count+=1
        start=i[1]+1
print(count)

'''
ip:"hippopotamus"
reverse the string without changing the position of vowels
op="simtopopapuh"
'''
a="hippopotamus"
vowels = 'aeiou'
non_vowels = []
for i in a:
    if i not in vowels:
        non_vowels.append(i)
non_vowels = non_vowels[::-1]
print(non_vowels)
res = ''
j = 0
for i in a:
    if i in vowels:
        res+=i
    else:
        res += non_vowels[j]
        j += 1
print(res)

#or optimal
a="hippopotamus"
vowels = 'aeiou'
b=list(a)
print(b)
i=0
j=len(b)-1
while i<j:
    if b[i] in vowels:
        i += 1
    elif b[j] in vowels:
        j -= 1
    else:
        b[i], b[j] = b[j], b[i]
        i += 1
        j -= 1
print("".join(b))

'''
ip:[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=5 pick a k books contigious (5 in row) to get the maximum discounts of the books
'''
a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=5
sum=0
for i in range(k):
    sum += a[i]
l=0
m=sum
for r in range(k,len(a)):
    sum = sum-a[l]+a[r]
    l+=1
    m=max(sum,m)
print(m)
'''
ip:[2,1,6,4,2,3,1,1,4,2,6,7,3]
print length of longest sub array(window can as much big as possible but sum should not go beyond)
sum<=k
'''
a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=7
l=0
sum=0
m=0
for r in range(len(a)):
    sum += a[r]
    if sum<=k:
        m= max(m,r-l +1)
    else:
        sum -= a[l]
        l += 1
print(m)

'''
in:a='ababba'
print length of longest palindromic sub string
op:4 and also that sub string
'''
s="ababba"
m=0
start=0
c=0
for i in range(len(s)):
    #odd length
    l=i
    r=i
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1>m:
            m=r-l+1
            start=l
        c+=1
        l=l-1
        r=r+1
    #even length
    l=i
    r=i+1
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1>m:
            m=r-l+1
            start=l
        c+=1
        l=l-1
        r=r+1

print(m)
print(s[start:start+m])
print(c)

'''
ip:"abcdaecdb"
print length of longest sub string without repeating char
'''
s="abcdecfbgce"
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
    if r-l+1>m:
        m=r-l+1
        start=l
print(m)
print(s[start:start+m])
#or
s="abcdcecdb"
m=0
d={}
l=0
for r in range(len(s)):
    if s[r] in d and d[s[r]]>l:
        l=d[s[r]]+1
    d[s[r]]=r
    m=max(m,r-l+1)
print(m)
    
    