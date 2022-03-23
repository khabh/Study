a=int(input())
cnt=0
total=0
for i in range (1,a+1):
    total+=i
    cnt+=1
    if (total>a):
        cnt-=1
        break;
print(N)    
