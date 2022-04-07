case=int(input())
for _ in range (case):
    people,num=map(int,input().split())
    sit=[0 for i in range(num)]
    count=0
    for i in range (people):
        want=int(input())-1
        if sit[want]==0:
            sit[want]=1
        else:
            count+=1
     
    print(count) 