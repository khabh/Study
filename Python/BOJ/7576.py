import sys


def bfs(n):
    global tomatoes
    count = -1
    while True:
        tomatoes -= len(n)
        count += 1
        temp = []
        for x, y in n:
            for deltaX, deltaY in delta:
                X = deltaX + x
                Y = deltaY + y
                if 0 <= X < N and 0 <= Y < M and graph[X][Y] == '0':
                    graph[X][Y] = '1'
                    temp.append((X, Y))
        if len(temp) == 0:
            break
        n = temp
    if tomatoes:
        return - 1
    return count


read = sys.stdin.readline
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
M, N = map(int, read().split())
graph = [list(read().split()) for _ in range(N)]
result = 0
tomatoes = M * N
first = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            continue
        elif graph[i][j] == '1':
            first.append((i, j))
            continue
        tomatoes -= 1

print(bfs(first))
