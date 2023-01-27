import sys


def bfs(start):
    global max_dist
    distance = [-1 for _ in range(N + 1)]
    distance[start] = 0
    stack = [start]

    while stack:
        n = stack[-1]
        clear = True
        for node, d in graph[n]:
            if distance[node] == -1:
                distance[node] = 0
                clear = False
                stack.append(node)
        if clear:
            max1 = max2 = 0
            stack.pop()
            for node, d in graph[n]:
                temp = distance[node] + d
                if temp > max1:
                    max2 = max1
                    max1 = temp
                elif temp > max2:
                    max2 = temp
            if (temp := max1 + max2) > max_dist:
                max_dist = temp
            distance[n] = max1


read = sys.stdin.readline
N = int(read())
max_dist = -1
graph = [[] for _ in range(N + 1)]
first = 0
for _ in range(N - 1):
    a, b, c = map(int, read().split())
    if not first:
        first = a
    graph[a].append((b, c))

bfs(first)
print(max_dist)
