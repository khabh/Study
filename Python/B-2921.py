a=int(input())
lsit=[]
for i in range(a+1):
    for j in range(a,i-1,-1):
        lsit.append(i+j)
print(sum(lsit))
