import sys
from collections import deque


def move_up(a, b):
    x, y = a
    while graph[x - 1][y] == '.':
        x -= 1
    a = (x if graph[x - 1][y] == '#' else (x - 1), y)
    x, y = b
    while graph[x - 1][y] == '.':
        x -= 1
    b = (x if graph[x - 1][y] == '#' else (x - 1), y)
    if a == b and a != out:
        return a, (b[0] + 1, y)

    return a, b


def move_down(a, b):
    x, y = a
    while graph[x + 1][y] == '.':
        x += 1
    a = (x if graph[x + 1][y] == '#' else x + 1, y)
    x, y = b
    while graph[x + 1][y] == '.':
        x += 1
    b = (x if graph[x + 1][y] == '#' else (x + 1), y)
    if a == b and a != out:
        return a, (b[0] - 1, y)

    return a, b


def move_right(a, b):
    x, y = a
    while graph[x][y + 1] == '.':
        y += 1
    a = (x, y if graph[x][y + 1] == '#' else y + 1)
    x, y = b
    while graph[x][y + 1] == '.':
        y += 1
    b = (x, y if graph[x][y + 1] == '#' else (y + 1))
    if a == b and a != out:
        return a, (x, b[1] - 1)

    return a, b


def move_left(a, b):
    x, y = a
    while graph[x][y - 1] == '.':
        y -= 1
    a = (x, y if graph[x][y - 1] == '#' else y - 1)
    x, y = b
    while graph[x][y - 1] == '.':
        y -= 1
    b = (x, y if graph[x][y - 1] == '#' else (y - 1))
    if a == b and a != out:
        return a, (x, b[1] + 1)

    return a, b


def bfs(r, b):
    def check(red, blue):
        if red == out and blue != out:
            return 1
        if red != blue and blue != out and (red, blue) not in visit:
            visit.add((red, blue))
            queue.append((red, blue, count + 1))
            return 0
        return 0

    queue = deque([(r, b, 0)])
    visit = {(r, b)}
    while queue:
        r, b, count = queue.popleft()
        if count == 10:
            return -1
        if r[0] < b[0]:
            R, B = move_up(r, b)
            if check(R, B):
                return count + 1
            B, R = move_down(b, r)
            if check(R, B):
                return count + 1
        else:
            B, R = move_up(b, r)
            if check(R, B):
                return count + 1
            R, B = move_down(r, b)
            if check(R, B):
                return count + 1
        if r[1] < b[1]:
            R, B = move_left(r, b)
            if check(R, B):
                return count + 1
            B, R = move_right(b, r)
            if check(R, B):
                return count + 1
        else:
            B, R = move_left(b, r)
            if check(R, B):
                return count + 1
            R, B = move_right(r, b)
            if check(R, B):
                return count + 1
    return -1


read = sys.stdin.readline
N, M = map(int, read().split())
graph = []
red, blue, out = 0, 0, 0
for i in range(N):
    graph.append(list(read().rstrip()))
    for j in range(M):
        if graph[i][j] == 'R':
            graph[i][j] = '.'
            red = (i, j)
        elif graph[i][j] == 'B':
            graph[i][j] = '.'
            blue = (i, j)
        elif graph[i][j] == 'O':
            out = (i, j)
print(bfs(red, blue))
