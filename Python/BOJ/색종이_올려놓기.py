import sys

read = sys.stdin.readline
N = int(read())
paper = []
for _ in range(N):
    a, b = map(int, read().split())
    if a > b:
        paper.append((a, b))
    else:
        paper.append((b, a))
paper.sort(reverse=True)
dp = [1] * N
for i in range(1, N):
    a, b = paper[i]
    for j in range(i - 1, -1, -1):
        if a <= paper[j][0] and b <= paper[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))

