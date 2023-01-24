from sys import stdin
from collections import deque


def dfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = graph[queue.popleft()]
        if not visited[node]:
            visited[node] = True
            queue.append(node)


read = stdin.readline
for _ in range(int(read())):
    N = int(read())
    count = 0
    graph = [0]
    visited = [False] * (N + 1)
    for i in map(int, read().split()):
        graph.append(i)
    for j in range(1, N + 1):
        if not visited[j]:
            count += 1
            dfs(j)
    print(count)
