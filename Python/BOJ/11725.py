from sys import stdin
from collections import deque


def bfs():
    queue = deque([1])
    while queue:
        n = queue.popleft()
        for node in graph[n]:
            if parent[node] == 0:
                parent[node] = n
                queue.append(node)


read = stdin.readline
N = int(read())
parent = [0 for _ in range(N + 1)]
parent[1] = 1
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
bfs()
print(*parent[2:], sep='\n')
