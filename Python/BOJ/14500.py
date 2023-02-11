import sys


def dfs(x, y, count, value):
    global result
    if value + (4 - count) * max_number <= result:
        return
    if count == 4:
        result = max(result, value)
        return
    for deltaX, deltaY in delta:
        X = x + deltaX
        Y = y + deltaY
        if 0 <= X < N and 0 <= Y < M and (X, Y) not in visit:
            if count == 2:
                visit.add((X, Y))
                dfs(x, y, count + 1, value + paper[X][Y])
                visit.remove((X, Y))
            visit.add((X, Y))
            dfs(X, Y, count + 1, value + paper[X][Y])
            visit.remove((X, Y))


read = sys.stdin.readline
N, M = map(int, read().split())
paper = [list(map(int, read().split())) for _ in range(N)]
max_number = max(map(max, paper))
visit = set()
visit.add((0, 0))
result = 0
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for i in range(N):
    for j in range(M):
        visit.add((i, j))
        dfs(i, j, 1, paper[i][j])
        visit.remove((i, j))
print(result)
