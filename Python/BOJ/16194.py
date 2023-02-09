import sys

read = sys.stdin.readline
N = int(read())
price = [0] + list(map(int, read().split()))
dp = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i] = price[i]
    for j in range(1, i + 1):
        dp[i] = min(dp[j] + price[i - j], dp[i])
print(dp[N])
