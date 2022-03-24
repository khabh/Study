num=int(input())
n=0
for i in range (num):
    a=list(map(int,input().split()))
    a.sort()
    if a[0]==a[2]:
        k=a[0]*1000+10000
    elif a[0]==a[1] or a[1]==a[2]:
        k=a[1]*100+1000
    else:
        k=a[2]*100
        
    if k>=n:
        n=k
        
print(n)
