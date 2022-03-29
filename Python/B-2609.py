a,b=map(int,input().split())
n=a
m=b
while(m!=0):
   r=n%m
   n=m
   m=r

print(n)
print(int(a*b/n))
