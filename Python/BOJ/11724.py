from sys import stdin
from collections import deque


def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        current_node = queue.popleft()
        for node in graph[current_node]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


read = stdin.readline
N, M = map(int, read().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
total = 0

for _ in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    if not visited[i]:
        total += 1
        bfs(i)

print(total)
