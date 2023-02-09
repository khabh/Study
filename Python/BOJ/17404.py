import sys

read = sys.stdin.readline
N = int(read())
price = [list(map(int, read().split())) for _ in range(N)]
result = 10000001
for j in range(3):
    dp = [10000001, 10000001, 10000001]
    dp[j] = price[0][j]
    for i in range(1, N):
        dp = [min(dp[1], dp[2]) + price[i][0], min(dp[0], dp[2]) + price[i][1], min(dp[0], dp[1]) + price[i][2]]
    for i in range(3):
        if j != i:
            result = min(result, dp[i])
print(result)
