import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


n, m = map(int, input().split())
start = int(input())  # 1에서 시작
graph = [[] for i in range(n + 1)]  # 노드 간 관계 저장
distance = [INF] * (n+1)  # 시작 노드에서 인덱스에 해당하는 노드까지 가는 데 필요한 최소 거리

for _ in range(m):
    a, b, c = map(int, input().split())  # a노드에서 b노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
