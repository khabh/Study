from sys import stdin
from collections import deque


def bfs(start):
    queue = deque([start])
    if visited[start] == 2:
        visited[start] = 0
    while queue:
        n = queue.popleft()
        opposite = (visited[n] + 1) % 2
        for node in graph[n]:
            if visited[node] == 2:
                queue.append(node)
                visited[node] = opposite
            elif visited[node] != opposite:
                return False

    return True


read = stdin.readline
for _ in range(int(read())):
    V, E = map(int, read().split())
    result = 'YES'
    visited = [2] * (V + 1)
    graph = [[] for _ in range(V + 1)]
    for j in range(E):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, V + 1):
        if not bfs(i):
            result = 'NO'
            break
    print(result)




