case,total=map(int,input().split())
cnt=0
coin=[]
for i in range (case):
    coin.append(int(input()))
coin.reverse()
for j in coin:
    cnt+=total//j
    total-=j*(total//j)
print(cnt)