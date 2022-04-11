# 캐릭터는 N*M 크기의 직사각형 내에서 움직인다
# 각 칸은 (A,B)로 나타낼 수 있고 바다로 되어 있는 공간은 갈 수 없다.

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
visit = [[0 for i in range(m)] for _ in range(n)]
visit[x][y] = 1


place = []
for _ in range(n):
    place.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turnLeft():
    # direction 값 0북 1동 2남 3서
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1  # 캐릭터가 거쳐간 칸의 개수이므로 시작점도 더해야 한다
turnTime = 0
while True:
    turnLeft()
    nx = x+dx[direction]
    ny = y+dy[direction]
    if visit[nx][ny] == 0 and place[nx][ny] == 0:
        x = nx
        y = ny
        visit[x][y] = 1
        turnTime = 0
        count += 1
        continue
    else:
        turnTime += 1
    if turnTime == 4:
        nx = x-dx[direction]
        ny = y-dy[direction]
        if place[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turnTime = 0

print(count)
