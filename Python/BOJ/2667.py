from sys import stdin


def bfs(x, y):
    count = 1
    location = [(x, y)]
    graph[x][y] = '0'
    while location:
        x, y = location.pop()
        for deltaX, deltaY in delta:
            next_x, next_y = x + deltaX, y + deltaY
            if 0 <= next_x < N and 0 <= next_y < N and graph[next_x][next_y] == '1':
                graph[next_x][next_y] = '0'
                location.append((next_x, next_y))
                count += 1
    return count


input = stdin.readline
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            result.append(bfs(i, j))
result.sort()
print(len(result))
print(*result, sep='\n')
