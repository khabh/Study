import sys
from collections import deque


def bfs(start):
    x1, y1, x2, y2 = start
    visit = set()
    visit.add((x1, y1, x2, y2))
    queue = deque([(x1, y1, x2, y2, 0)])
    while queue:
        x1, y1, x2, y2, count = queue.popleft()
        if count >= 10:
            return '-1'
        for deltaX, deltaY in delta:
            out = 0
            X1, Y1, X2, Y2 = x1 + deltaX, y1 + deltaY, x2 + deltaX, y2 + deltaY
            if 0 <= X1 < N and 0 <= Y1 < M:
                if graph[X1][Y1] == '#':
                    X1, Y1 = x1, y1
            else:
                out += 1
            if 0 <= X2 < N and 0 <= Y2 < M:
                if graph[X2][Y2] == '#':
                    X2, Y2 = x2, y2
            else:
                out += 1
            if X1 == X2 and Y1 == Y2:
                continue
            if out == 1:
                return count + 1
            elif not out and (X1, Y1, X2, Y2) not in visit:
                queue.append((X1, Y1, X2, Y2, count + 1))
                visit.add((X1, Y1, X2, Y2))
    return '-1'


read = sys.stdin.readline
N, M = map(int, read().split())
graph = []
coin = []
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for i in range(N):
    graph.append(list(read().rstrip()))
    for j in range(M):
        if graph[i][j] == 'o':
            coin.append(i)
            coin.append(j)
print(bfs(coin))
