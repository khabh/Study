# 캐릭터는 N*M 크기의 직사각형 내에서 움직인다
# 각 칸은 (A,B)로 나타낼 수 있고 바다로 되어 있는 공간은 갈 수 없다.

n, m = map(int, input().split())
visit = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
visit[x][y] = 1

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

up:
