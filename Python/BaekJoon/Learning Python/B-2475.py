k=map(int,input().split())
total=0
for i in k:
    total+=i**2

print(total%10)
