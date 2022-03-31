a=int(input())
k=map(int,input().split())
count=0

for num in k:
    check=0
    if num>1:
        for i in range(2,num):
            if num%i==0:
                check+=1
        if check==0:
            count+=1

print(count)
