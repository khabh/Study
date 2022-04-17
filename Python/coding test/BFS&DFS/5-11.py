# 입력받기
from collections import deque


n, m = map(int, input().split())
field = []
for _ in range(n):
    field.append(list(map(int, input())))
# 상,하,좌,우 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if field[nx][ny] == 1:
                field[nx][ny] += field[x][y]
                queue.append((nx, ny))

    return field[n-1][m-1]


print(bfs(0, 0))
