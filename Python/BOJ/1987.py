import sys


def bfs():
    result = 1
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    queue = set()
    queue.add((0, 0, graph[0][0]))
    while queue:
        x, y, log = queue.pop()
        value = len(log) + 1
        for deltaX, deltaY in delta:
            X, Y = x + deltaX, y + deltaY
            if 0 <= X < R and 0 <= Y < C and graph[X][Y] not in log:
                queue.add((X, Y, log + graph[X][Y]))
                if result < value:
                    result = value
    return result


R, C = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().rstrip() for _ in range(R)]
print(bfs())
