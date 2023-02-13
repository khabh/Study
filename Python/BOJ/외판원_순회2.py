import sys


def dfs(cost, city, count):
    global result, start
    if cost > result:
        return
    if count == N:
        if graph[city][start]:
            cost += graph[city][start]
            result = min(result, cost)
        return
    for index, value in enumerate(graph[city]):
        if value and not visit[index]:
            visit[index] = True
            dfs(value + cost, index, count + 1)
            visit[index] = False


read = sys.stdin.readline
N = int(read())
graph = [list(map(int, read().split())) for _ in range(N)]
visit = [False] * N
result = sys.maxsize
for i in range(N):
    start = i
    visit[i] = True
    dfs(0, i, 1)
    visit[i] = False
print(result)
