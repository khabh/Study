import sys


def dfs(x, y):
    count = visit[x][y]
    for deltaX, deltaY in delta:
        X = x + deltaX
        Y = y + deltaY
        if 0 <= X < N and 0 <= Y < M and graph[X][Y] == graph[x][y]:
            if visit[X][Y]:
                if count - visit[X][Y] >= 3:
                    print('Yes')
                    sys.exit()
            else:
                visit[X][Y] = count + 1
                dfs(X, Y)
                temp.add((X, Y))
                visit[X][Y] = 0


read = sys.stdin.readline
N, M = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            temp = set()
            temp.add((i, j))
            visit[i][j] = 1
            dfs(i, j)
            for a, b in temp:
                visit[a][b] = -1
print('No')
