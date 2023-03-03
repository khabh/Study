import sys

read = sys.stdin.readline
N, K = map(int, read().split())
rooms = [tuple(map(int, read().split())) for _ in range(N)]
dp = [[[0] * (K + 1) for _ in range(3)] for _ in range(N)]
if K:
    dp[0][0][1], dp[0][1][1] = rooms[0][0], rooms[0][1]
dp[0][2][0] = sum(rooms[0])
for i in range(1, N):
    dp[i][2][0] = dp[i - 1][2][0] + rooms[i][0] + rooms[i][1]
    for j in range(1, K + 1):
        dp[i][0][j] = max(dp[i - 1][0][j - 1], dp[i - 1][2][j - 1]) + rooms[i][0]
        dp[i][1][j] = max(dp[i - 1][1][j - 1], dp[i - 1][2][j - 1]) + rooms[i][1]
        if j == i + 1:
            continue
        dp[i][2][j] = max(dp[i - 1][1][j], dp[i - 1][0][j], dp[i - 1][2][j]) + rooms[i][0] + rooms[i][1]
print(max(dp[-1][0][K], dp[-1][1][K], dp[-1][2][K]))
