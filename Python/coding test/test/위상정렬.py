from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegreee = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegreee[b] += 1


def topology_sort():
    q = deque()
    for i in range(1, n+1):
        if indegreee[i] == 0:
            q.append(i)

    result = []

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegreee[i] -= 1
            if indegreee[i] == 0:
                q.append(i)

    print(*result)


topology_sort()
