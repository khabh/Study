import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def smallest_dis():
    smallest = INF
    index = 0
    for i in range(1, n+1):
        if not visited[i] and distnace[i] < smallest:
            smallest = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for _ in range(n-1):
        now = smallest_dis()
        visited[now] = True
        for j in graph[now]:
            cost = j[1] + distance[now]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
for i in range(1, n+1):
    print(distance[i])
