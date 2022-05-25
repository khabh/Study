import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
distance = [INF]*(n+1)

graph = [[]for _ in range(n+1)]


for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijstra(c)
count = 0
result = 0

for i in distance:
    if i != INF:
        count += 1
        result = max(result, i)

print(count-1, result)
