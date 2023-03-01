import sys


def make_cross(x, y, length):
    graph[x][y] = '.'
    for i in range(1, length + 1):
        for deltaX, deltaY in delta:
            X = x + deltaX * i
            Y = y + deltaY * i
            graph[X][Y] = '.'


def remove_cross(x, y, length):
    for deltaX, deltaY in delta:
        X = x + deltaX * length
        Y = y + deltaY * length
        graph[X][Y] = '#'
    if length == 1:
        graph[x][y] = '#'


def is_cross(x, y):
    if graph[x][y] == '.':
        return 0
    length = 1
    while 1:
        for deltaX, deltaY in delta:
            X = x + deltaX * length
            Y = y + deltaY * length
            if (not (0 <= X < N and 0 <= Y < M)) or graph[X][Y] == '.':
                return length - 1
        length += 1


def have_min_cross():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '#':
                return True
    return False


def dfs(x, y, count, prev):
    global result
    if count >= 1:
        if count == 1 and not have_min_cross():
            return
        result = max(prev, result)
        if count == 2:
            return
    for j in range(y, M):
        length = is_cross(x, j)
        if length:
            area = 1 + 4 * length
            make_cross(x, j, length)
            for l in range(length, 0, -1):
                dfs(x, j + 1, count + 1, prev * area)
                remove_cross(x, j, l)
                area -= 4
    for i in range(x + 1, N):
        for j in range(M):
            length = is_cross(i, j)
            if length:
                area = 1 + 4 * length
                make_cross(i, j, length)
                for l in range(length, 0, -1):
                    dfs(i, j + 1, count + 1, prev * area)
                    remove_cross(i, j, l)
                    area -= 4


read = sys.stdin.readline
N, M = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(N)]
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
result = 1
dfs(1, 0, 0, 1)
print(result)
