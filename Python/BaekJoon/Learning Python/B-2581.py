M=int(input())
N=int(input())
lsit=[]
for num in range(M,N+1):
    check=0
    if num>1:
        for i in range(2,num):
            if num%i==0:
                check+=1
        if check==0:
            lsit.append(num)
        
        
if lsit==[]:
    print(-1)
else:
    print(sum(lsit))
    print(lsit[0])
