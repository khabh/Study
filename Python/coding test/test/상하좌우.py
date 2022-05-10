n = int(input())
plan = list(input().split())

x = y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for i in plan:
    k = move.index(i)
    nx = x + dx[k]
    ny = y + dy[k]
    if 1 <= nx <= n and 1 <= ny <= n:
        x = nx
        y = ny

print(x, y)
