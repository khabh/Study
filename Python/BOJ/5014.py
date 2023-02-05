import sys
from collections import deque


def bfs():
    queue = deque([(S, 0)])
    visit = [False] * (F + 1)
    visit[S] = True
    while queue:
        n, cnt = queue.popleft()
        if n == G:
            return cnt
        u = n + U
        if u <= F and not visit[u]:
            visit[u] = True
            queue.append((u, cnt + 1))
        d = n - D
        if d > 0 and not visit[d]:
            visit[d] = True
            queue.append((d, cnt + 1))

    return 'use the stairs'


read = sys.stdin.readline
F, S, G, U, D = map(int, read().split())
print(bfs())
