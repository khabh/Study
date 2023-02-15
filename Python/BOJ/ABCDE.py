import sys


def dfs(n, count):
    if count == 4:
        print('1')
        sys.exit()
    for node in graph[n]:
        if not visit[node]:
            visit[node] = True
            dfs(node, count + 1)
            visit[node] = False


read = sys.stdin.readline
N, M = map(int, read().split())
graph = [[] for _ in range(N)]
visit = [False] * N
result = 0
for _ in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N):
    visit[i] = True
    dfs(i, 0)
    visit[i] = False
print('0')
