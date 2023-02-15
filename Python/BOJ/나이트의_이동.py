import sys
from collections import deque


def dfs(a, b):
    visit = set()
    queue = deque([(a, b, 0)])
    visit.add((a, b))
    while queue:
        x, y, count = queue.popleft()
        if x == x2 and y == y2:
            return count
        for delta_x, delta_y in delta:
            X = delta_x + x
            Y = delta_y + y
            if 0 <= X < I and 0 <= Y < I and (X, Y) not in visit:
                visit.add((X, Y))
                queue.append((X, Y, count + 1))


read = sys.stdin.readline
delta = [(1, 2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, -1), (1, -2), (-2, 1)]
for _ in range(int(read())):
    I = int(read())
    x1, y1 = map(int, read().split())
    x2, y2 = map(int, read().split())
    print(dfs(x1, y1))
