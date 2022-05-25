from collections import deque

n = int(input())
cost = [0] * (n+1)
indegree = [0]*(n+1)
graph = [[]for _ in range(n+1)]


for i in range(1, n+1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)


def topology():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = cost[:]
    while q:
        now = q.popleft()
        for j in graph[now]:
            indegree[j] -= 1
            result[j] = max(result[now]+cost[j], result[j])
            if indegree[j] == 0:
                q.append(j)

    print(*result)


topology()
