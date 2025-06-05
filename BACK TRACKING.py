#NO OF ISLANDS
'''ip:
   1 0 0 1 1
   1 0 0 0 1
   0 0 0 1 0
   1 0 0 0 0
   1 0 0 0 1
matrix if there are =land 0= water 1 1s at corners we can join and form the island and print no of isalnds
op:5'''
def island(a,i,j,n):
    if i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2:
        return 0
    if a[i][j]==1:
        a[i][j]=2
    island(a,i-1,j,n)
    island(a,i,j-1,n)
    island(a,i+1,j,n)
    island(a,i,j+1,n)
a = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]
n=5
c=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            island(a,i,j,n)
            c=c+1            
print(c)
print()

'''a=[7,6,5,2,1]
ip:
    0 1 1 0 1=> sum=12(6+5+1)
    1 1 0 0 1=> sum=14(7+6+1)
    0 0 0 1 1=> sum=3(2+1)
    0 1 0 0 0=> sum=6(6)'''
a= [[1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1]
    ]
b=[7,6,5,2,1]
for i in range(len(a)):
    s=0
    for j in range(len(a[0])):
        if a[i][j]==1:
            s+=b[j]
    print(s)
print()

#Rat and Maze
'''ip:
    1 0 0 0 0
    1 1 1 0 0
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 0 1
if rat at starting point a[0][0] and it should reach a[n][n] by going just right and down if there is 1 only'''

def rat(a,i,j,n):
    if j>=n or i>=n or a[i][j]==0 :
        return 0
    if i==n-1 and j==n-1 and a[i][j]==1:
        return 1
    return rat(a,i,j+1,n)+rat(a,i+1,j,n)
a = [
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1]
]
print(rat(a,0,0,5))
print()

#Forest in Fire
'''ip:
   1 0 0 1 1 1
   1 1 1 0 0 0
   0 0 1 1 1 1
   1 1 1 0 0 0
   0 0 0 0 0 1
   1 0 0 1 0 0
   given 0 is bareland and 1 is tree and given a location like 3,6 3rd row 6th col tree gets burned
   and it goes top ,bottom,left and right it will spread print how many trees are unburnt
   '''
def burn(a,i,j,n):
    if i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2 :
        return 0
    if a[i][j]==1:
        a[i][j]=2
    burn(a,i-1,j,n)
    burn(a,i,j-1,n)
    burn(a,i+1,j,n)
    burn(a,i,j+1,n)
a=[[1 ,0 ,0, 1, 1, 1],
   [1 ,1 ,1, 0, 0, 0],
   [0 ,0 ,1, 1 ,1, 1],
   [1 ,1, 1, 0, 0, 0],
   [0 ,0 ,0 ,0 ,0, 1],
   [1 ,0 ,0 ,1 ,0, 0]]
c=0
n=6
i=3
j=6
burn(a,i-1,j-1, n)
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            c=c+1            
print(c)

#FROG
'''there is a box 5 rows and 5 cols a frog is at 2nd row 3rd col and
[(2,1),(4,1),(5,2),(3,5)]these are paths if frog goes it will die and it can only jump right and down
so how many paths are possible to go to the (5,5)'''

def frog(n,i,j,die):
    if  i>=n or j>=n or (i-1,j-1) in die:
        return 0
    if i==n-1 and j==n-1:
        return 1
    return frog(n,i+1,j,die) + frog(n,i,j+1,die)
n=5
i,j=(2,3)
die=[(2,1),(4,1),(5,2),(3,5)]
print(frog(n,i-1,j-1,die))
print()

#ALL BINARY
''' ip:3      ip:12
    op:00     op:0000
       01        0001
       10        0010
       11        0011
                 0100
                 0101
                 0110
                 0111
                 1000
                 1001
                 1010
'''
import math
re=[]
def allbinary(n,s=''):
    if len(s)==n:
        re.append(s)
        return
    allbinary(n,s+'0')
    allbinary(n,s+'1')
a=8
n=int(math.log(a,2))+1
allbinary(n)
for i in range(a+1):
    print(re[i])
#or
import math
def allbinary(a,n,s=''):
    if a==-1:
        return a
    if len(s)==n:
        print(s)
        a=a-1
        return a
    a=allbinary(a,n,s+'0')
    a=allbinary(a,n,s+'1')
    return a
a=5
n=int(math.log(a,2))+1
allbinary(a,n)
print()

#BALANCED PARANTHESIS
'''
ip:3
op:
  ((()))
  (()())
  (())()
  ()(())
  ()()()
'''    
def brackets(n,open=0,close=0,cur=""):
    if len(cur)==2*n:
        print(cur)
        return
    if open<n:
        brackets(n,open+1,close,cur+"(")
    if close<open:
        brackets(n,open,close+1,cur+")")
n=4
brackets(n)
