import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = 0
    while visited[K] == -1:
        n = queue.popleft()
        time = visited[n] + 1
        if n - 1 >= 0 and visited[n - 1] == -1:
            visited[n - 1] = time
            queue.append(n - 1)
        if n + 1 < 100001 and visited[n + 1] == -1:
            visited[n + 1] = time
            queue.append(n + 1)
        if n * 2 < 100001 and visited[n * 2] == -1:
            visited[n * 2] = time
            queue.append(n * 2)


N, K = map(int, input().split())
if K <= N:
    print(N - K)
    sys.exit()
visited = [-1] * 100001
bfs(N)
print(visited[K])
