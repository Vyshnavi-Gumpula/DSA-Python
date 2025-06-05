#Sum of even numbers in the list
def even_sum(a,i):
    if i==len(a):
        return 0
    if a[i]%2==0:
        return a[i]+even_sum(a,i+1)
    else:
        return even_sum(a,i+1)       
a=[2,5,6,7,2,1,4,3,6]
print(even_sum(a,0))
print('---')
#REVERSE OF A NUMBER USING RECURSION
def reverse(re, n):
    if n == 0:
        return re
    return reverse(re*10+n%10,n//10)
n = int(input())
print(reverse(0, n))
print('---')
#Number is prime or not
def is_prime(n,i=2):
    if n<=1:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    return is_prime(n,i+1)
print(is_prime(7)) 
print('----')
#COUNT OF PRIME NUMBERS IN LIST 
def count_primes(lst, index=0):
    if index == len(lst):
        return 0
    if is_prime(lst[index]):
        return 1 + count_primes(lst,index + 1)
    else:
        return count_primes(lst, index + 1)
num= [13, 17, 21, 23, 22, 7, 19]
print(count_primes(num))

print('--')
#minimum no of subtractions
'''input:20
input 3,5
whether its possible to reach 1 or not by subtracting 3 or 5 from 20 if it is possible True or else False,
minimum no of possible ways '''
def count(n,p,q):
    if n==1:
        return True
    if n<1:
        return False
    return count(n-p,p,q) or count(n-q,p,q)
print(count(20,3,5))
def count(n,p,q,c=0):
    if n==1:
        return 0
    if n<1:
        return False
    else:
        return 1+min(count(n-p,p,q,c+1) , count(n-q,p,q,c+1))  
n=20
p=3
q=5
print(count(n,p,q))