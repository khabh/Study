import sys
from collections import deque


def bfs():
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(0, 0, 0)])
    visit = set()
    visit.add((0, 0))
    while queue:
        x, y, count = queue.popleft()
        if x == M - 1 and y == N - 1:
            return count
        for deltaX, deltaY in delta:
            X = x + deltaX
            Y = y + deltaY
            if 0 <= X < M and 0 <= Y < N and (X, Y) not in visit:
                visit.add((X, Y))
                if graph[X][Y] == '0':
                    queue.appendleft((X, Y, count))
                else:
                    queue.append((X, Y, count + 1))


read = sys.stdin.readline
N, M = map(int, read().split())
graph = list(read().rstrip() for _ in range(M))
print(bfs())
