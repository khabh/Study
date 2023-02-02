import sys
from collections import deque


def bfs(start):
    global cnt
    queue = deque()
    visit = [[[0] * M for _ in range(N)] for _ in range(max_index)]
    for a, b in start:
        queue.append((a, b, 0))
        visit[0][a][b] = 1
    while queue:
        x, y, i = queue.popleft()
        if i == max_index - 1:
            cnt += visit[i][x][y]
            continue
        for deltaX, deltaY in delta:
            X, Y = x + deltaX, y + deltaY
            if 0 <= X < N and 0 <= Y < M and word[X][Y] == find[i + 1]:
                if visit[i + 1][X][Y] == 0:
                    queue.append((X, Y, i + 1))
                visit[i + 1][X][Y] += visit[i][x][y]


read = sys.stdin.readline
N, M, K = map(int, read().split())
delta = deque([(0, 1), (0, -1), (1, 0), (-1, 0)])
for i in range(2, K + 1):
    delta.append((0, i))
    delta.append((0, -i))
    delta.append((i, 0))
    delta.append((-i, 0))
word = [list(read().rstrip()) for _ in range(N)]
find = read().rstrip()
max_index = len(find)
cnt = 0
first = deque()
for i in range(N):
    for j in range(M):
        if word[i][j] == find[0]:
            first.append((i, j))
bfs(first)
print(cnt)