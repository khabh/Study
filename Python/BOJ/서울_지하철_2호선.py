import sys
from collections import deque
sys.setrecursionlimit(10**6)


def bfs(start):
    queue = deque([(start, 0)])
    while queue:
        n, count = queue.popleft()
        for node in graph[n]:
            if result[node] == -1:
                result[node] = count + 1
                queue.append((node, count + 1))


def dfs(n):
    global cycle
    temp.append(n)
    for node in graph[n]:
        if not visit[node]:
            visit[node] = True
            if dfs(node):
                return True
            visit[node] = False
        elif node != temp[-2]:
            cycle = node
            return True
    temp.pop()
    return False


read = sys.stdin.readline
N = int(read())
graph = [[] for _ in range(N + 1)]
result = [-1] * (N + 1)
for _ in range(N):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [False] * (N + 1)
temp = []
cycle = -1
visit[1] = True
dfs(1)
for number in temp[::-1]:
    result[number] = 0
    if number == cycle:
        break
for i in range(1, N + 1):
    if result[i]:
        continue
    for station in graph[i]:
        if result[station] == -1:
            bfs(i)
            break
print(' '.join(map(str, result[1:])))
