a = "15,-3,+,6,2,-,*"
#a="15,3,+,6,2,-,*"
a=a.split(',')
print(a)
s = []
for i in a:
    if i[-1].isdigit():
        s.append(int(i))
    else:
        p1= s.pop()
        p2= s.pop() 
        if i== '+':
            s.append(p2+p1)
        elif i == '-':
            s.append(p2-p1)
        elif i== '*':
            s.append(p2*p1)
        elif i=='/':
            s.append(p2/p1)
        else:
            s.append(p2**p1)
print(s[-1])
# valid parenthesis
valid = [('{', '}'), ('(', ')'), ('[', ']')]
a = ")(({}))"
s = []
for i in a:
    if i in "({[":
        s.append(i)
    elif i in ")}]":
        if len(s) > 0 and (s[-1],i) in valid:
            s.pop()
        else:
            print("False")
            break
else:
    if len(s) == 0:
        print("True")
    else:
        print("False")
#or    
a = "(({})){}["
s = []
for i in range(len(a)):
    if a[i] in {'(','{','['}:
        s.append(a[i])
    elif s:
        if a[i]=='}' and s[-1]=='{':
            s.pop()
        elif a[i]==')' and s[-1]=='(':
            s.pop()
        elif a[i]==']' and s[-1]=='[':
            s.pop()
        else:
            print("invalid")
            break
    else:
        print("invalid")
        break
else:
    if s:
        print("invalid")
    else:
        print("valid")
    
a='{{{{}{}}}}((('
d={'}':'{',']':'[',')':'('}
s=[]
for i in range(len(a)):
    if (a[i] in {'(','{','['}):#{} set bcoz of time complexity
        s.append(a[i])
    else:
        if(s and d[a[i]]==s[-1]):
            s.pop()
        else:
            print('invalid')
            break
else:
    if(s):
        print('invalid')
    else:
        print('valid')

        
    