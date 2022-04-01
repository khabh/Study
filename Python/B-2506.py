case=int(input())
score=list(map(int,input().split()))
count=1
total=0

for i in range(0,case):
    if score[i]==1:
        total+=count
        count+=1
    else:
        count=1
        
print(total)
