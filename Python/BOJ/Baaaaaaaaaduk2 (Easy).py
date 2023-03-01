import sys
from collections import deque


def bfs(a, b):
    edge = set()
    queue = deque([(a, b)])
    graph[a][b] = '3'
    count = 1
    while queue:
        x, y = queue.popleft()
        for deltaX, deltaY in delta:
            X = x + deltaX
            Y = y + deltaY
            if 0 <= X < N and 0 <= Y < M:
                if graph[X][Y] == '2':
                    count += 1
                    graph[X][Y] = '3'
                    queue.append((X, Y))
                elif graph[X][Y] == '0':
                    edge.add((X, Y))
    if len(edge) <= 2:
        group.append((count, edge))


def dfs(index, visit, count):
    global result
    if len(visit) <= 2 and count > result:
        result = count
    if len(visit) > 2 or index == len(group):
        return
    dfs(index + 1, visit, count)
    for edge in group[index][1]:
        visit[edge] = visit.get(edge, 0) + 1
    count += group[index][0]
    dfs(index + 1, visit, count)
    for edge in group[index][1]:
        if visit[edge] == 1:
            del visit[edge]
        else:
            visit[edge] -= 1
    count -= group[index][0]


read = sys.stdin.readline
N, M = map(int, read().split())
graph = [list(read().split()) for _ in range(N)]
group = []
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == '2':
            bfs(i, j)
result = 0
dfs(0, {}, 0)
print(result)
