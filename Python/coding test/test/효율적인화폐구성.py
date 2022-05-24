n, m = map(int, input().split())
result = [0] * (m+1)

for i in range(n):
    coin = int(input())
    if coin > m:
        continue
    for j in range(coin, (m+1), coin):
        if result[j] == 0:
            result[j] = result[j-coin]+1
        else:
            result[j] = min(result[j-coin]+1, result[j])


if result[m] == 0:
    print(-1)
else:
    print(result[m])
