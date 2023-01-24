from collections import deque
import sys
read = sys.stdin.readline


def bfs():
    queue = deque([V])
    bfs_visited[V] = True
    while queue:
        n = queue.popleft()
        print(n, end=" ")
        for i in range(1, N + 1):
            if (not bfs_visited[i]) and graph[n][i]:
                queue.append(i)
                bfs_visited[i] = True


def dfs(n):
    dfs_visited[n] = True
    print(n, end=" ")
    for i in range(1, N + 1):
        if (not dfs_visited[i]) and graph[n][i]:
            dfs(i)


N, M, V = map(int, read().split())

graph = [[False for i in range(N + 1)] for _ in range(N + 1)]
dfs_visited = [False for _ in range(N + 1)]
bfs_visited = [False for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = True

dfs(V)
print()
bfs()
