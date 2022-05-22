from collections import deque
import copy

n = int(input())
array = [[] for _ in range(n+1)]
inputdata = [0] * (n+1)
indegree = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    inputdata[i] = data[0]
    if len(data) > 2:
        for j in data[1:-1]:
            array[j].append(i)
            indegree[i] += 1


# array에는 미리 들어야 하는 강의의 정보
# cost에는 들어야 하는 강의 시간


def topology_sort():
    cost = copy.deepcopy(inputdata)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for j in array[now]:
            indegree[j] -= 1
            cost[j] = max(cost[j], cost[now]+inputdata[j])
            if indegree[j] == 0:
                q.append(j)

    for i in range(1, n+1):
        print(cost[i])


topology_sort()
