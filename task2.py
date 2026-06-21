#Sum of Digits  
s=0
while n>0:
    s+=n%10
    n//=10
print(s)
#Reverse a Number 
n=1234
n=1234
r=0
while n>0:
    r=r*10+n%10
    n//=10
print(r)
#Count Digits in a Number  
n=12345
count=0
while n>0:
    count+=1
    n//=10
print(count)
#Check Even or Odd  
num=17
if num%2==0:
    print("even")
else:
    print("odd")
#Check Prime Number      
n=13
pri=0
for i in range(2,n):
 if n%i==0:
  pri=1
  break
if n>1 and pri==0:
   print("prime")
else:
   print("not prime")
#Find Factorial of a Number    
n=5
f=1
for i in range(1,n+1):
 f*=i
print(f)
#Find Factors of a Number   
num=12
for i in range(1,num+1):
 if num%i==0:
  print(i,end=" ")
print()
#Check Palindrome Number     
n=121
t=n
r=0
while n>0:
 r=r*10+n%10
 n//=10
if t==r:
  print("palindrome")
else:
  print("not palindorme")
#Check Armstrong Number        
n=153
t=n
s=0
while n>0:
 d=n%10
 s+=d**3
 n//=10
if t==s:
  print("armstrong")
else:
  print("not armstrong")
#Find GCD (HCF) of Two Numbers 
x,y=12,18
while y:
 x,y=y,x%y
print(x)
