import sys


def bfs():
    count = 0
    n = [(0, 0)]
    graph[0][0] = 0
    while graph[N - 1][M - 1] == '1':
        count += 1
        temp = []
        for x, y in n:
            for deltaX, deltaY in delta:
                X = x + deltaX
                Y = y + deltaY
                if 0 <= X < N and 0 <= Y < M and graph[X][Y] == '1':
                    if X == N - 1 and Y == M - 1:
                        return count + 1
                    graph[X][Y] = '0'
                    temp.append((X, Y))
        n = temp
    return count


read = sys.stdin.readline
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
N, M = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(N)]
print(bfs())
