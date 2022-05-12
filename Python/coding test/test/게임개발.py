d = []
n, m = map(int, input().split())
x, y, dir = map(int, input().split())

for i in range(n):
    d.append(list(map(int, input().split())))

sea = d[:]
d[x][y] = 1

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
turn = 0
result = 1

while True:
    dir -= 1
    if dir == -1:
        dir = 3

    turn += 1

    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < m:
        if d[nx][ny] == 0:
            x = nx
            y = ny
            d[x][y] = 1
            turn = 0
            result += 1
            continue

    if turn >= 4:
        turn = 0
        dir = (dir+2) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
        if sea[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny


print(result)
