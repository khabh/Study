INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]
print(graph)

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], grap[a][k]+grap[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            pirnt("INFINITY", end=' ')
        else:
            pirnt(graph[a][b], end=' ')

    print()
