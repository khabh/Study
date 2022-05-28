case, n = map(int, input().split())
array = []

for _ in range(case):
    array.append(int(input()))

d = [10001] * (n+1)

d[0] = 0

for i in range(n):
    for j in range(array[i],n+1):
        if d[j-array[i]] != 10001:
            d[j]=min(d[j-array[i]]+1,d[j])

        
if d[n] == 10001:
    print(-1)
else:
    print(d[m])
    



