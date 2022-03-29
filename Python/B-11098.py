a=int(input())
for _ in range(a):
    member=int(input())
    expense=0
    for i in range(member):
        price,name=map(str,input().split())
        if int(price)>expense:
            expense=int(price)
            choose=name
    print(choose)
