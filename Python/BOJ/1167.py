import sys
from collections import deque


def bfs(start):
    distance = [-1 for _ in range(V + 1)]
    queue = deque([start])
    distance[start] = 0
    while queue:
        n = queue.popleft()
        for node, d in graph[n]:
            if distance[node] == -1:
                distance[node] = distance[n] + d
                queue.append(node)
    max_distance = max(distance)
    return [distance.index(max_distance), max_distance]


read = sys.stdin.readline
V = int(read())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    numbers = list(map(int, read().split()))
    a = numbers[0]
    for i in range(1, len(numbers) - 1, 2):
        graph[a].append((numbers[i], numbers[i + 1]))
next_node = bfs(1)[0]
print(bfs(next_node)[1])
