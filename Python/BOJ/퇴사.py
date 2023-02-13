import sys


def dfs(date, total):
    global result
    if total > result:
        result = total
    for i in range(date + 1, N):
        if counsel[i][0] + i - 1 < N:
            dfs(counsel[i][0] + i - 1, total + counsel[i][1])


read = sys.stdin.readline
N = int(read())
counsel = []
for _ in range(N):
    a, b = map(int, read().split())
    counsel.append((a, b))
result = 0
dfs(-1, 0)
print(result)
