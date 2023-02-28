import sys


def find_up(x, y):
    for a in range(x - 1, -1, -1):
        if office[a][y] == '6':
            break
        if office[a][y] == '0':
            visit[(a, y)] = visit.get((a, y), 0) + 1


def find_down(x, y):
    for a in range(x + 1, N):
        if office[a][y] == '6':
            break
        if office[a][y] == '0':
            visit[(a, y)] = visit.get((a, y), 0) + 1


def find_left(x, y):
    for b in range(y - 1, -1, -1):
        if office[x][b] == '6':
            break
        if office[x][b] == '0':
            visit[(x, b)] = visit.get((x, b), 0) + 1


def find_right(x, y):
    for b in range(y + 1, M):
        if office[x][b] == '6':
            break
        if office[x][b] == '0':
            visit[(x, b)] = visit.get((x, b), 0) + 1


def remove_up(x, y):
    for a in range(x - 1, -1, -1):
        if office[a][y] == '6':
            break
        if office[a][y] == '0':
            if visit[(a, y)] == 1:
                del visit[(a, y)]
            else:
                visit[(a, y)] -= 1


def remove_down(x, y):
    for a in range(x + 1, N):
        if office[a][y] == '6':
            break
        if office[a][y] == '0':
            if visit[(a, y)] == 1:
                del visit[(a, y)]
            else:
                visit[(a, y)] -= 1


def remove_right(x, y):
    for b in range(y + 1, M):
        if office[x][b] == '6':
            break
        if office[x][b] == '0':
            if visit[(x, b)] == 1:
                del visit[(x, b)]
            else:
                visit[(x, b)] -= 1


def remove_left(x, y):
    for b in range(y - 1, -1, -1):
        if office[x][b] == '6':
            break
        if office[x][b] == '0':
            if visit[(x, b)] == 1:
                del visit[(x, b)]
            else:
                visit[(x, b)] -= 1


def kind_five(count, x, y):
    find_left(x, y)
    find_down(x, y)
    find_right(x, y)
    find_up(x, y)
    dfs(count + 1)
    remove_left(x, y)
    remove_down(x, y)
    remove_right(x, y)
    remove_up(x, y)


def kind_four(count, x, y):
    find_left(x, y)
    find_down(x, y)
    find_right(x, y)
    dfs(count + 1)
    remove_left(x, y)
    find_up(x, y)
    dfs(count + 1)
    remove_down(x, y)
    find_left(x, y)
    dfs(count + 1)
    remove_right(x, y)
    find_down(x, y)
    dfs(count + 1)
    remove_down(x, y)
    remove_up(x, y)
    remove_left(x, y)


def kind_one(count, x, y):
    find_left(x, y)
    dfs(count + 1)
    remove_left(x, y)
    find_up(x, y)
    dfs(count + 1)
    remove_up(x, y)
    find_down(x, y)
    dfs(count + 1)
    remove_down(x, y)
    find_right(x, y)
    dfs(count + 1)
    remove_right(x, y)


def kind_two(count, x, y):
    find_left(x, y)
    find_right(x, y)
    dfs(count + 1)
    remove_left(x, y)
    remove_right(x, y)
    find_up(x, y)
    find_down(x, y)
    dfs(count + 1)
    remove_up(x, y)
    remove_down(x, y)


def kind_three(count, x, y):
    find_left(x, y)
    find_down(x, y)
    dfs(count + 1)
    remove_left(x, y)
    find_right(x, y)
    dfs(count + 1)
    remove_down(x, y)
    find_up(x, y)
    dfs(count + 1)
    remove_right(x, y)
    find_left(x, y)
    dfs(count + 1)
    remove_up(x, y)
    remove_left(x, y)


def dfs(count):
    global max_camera
    if count == len(cctv):
        max_camera = max(max_camera, len(visit))
        return True
    x, y, kind = cctv[count]
    if kind == '5':
        kind_five(count, x, y)
    elif kind == '4':
        kind_four(count, x, y)
    elif kind == '1':
        kind_one(count, x, y)
    elif kind == '2':
        kind_two(count, x, y)
    else:
        kind_three(count, x, y)


read = sys.stdin.readline
N, M = map(int, read().split())
office = [read().split() for _ in range(N)]
cctv = []
not_blank = 0
max_camera = 0
visit = {}
for i in range(N):
    for j in range(M):
        if office[i][j] != '0' and office[i][j] != '6':
            cctv.append((i, j, office[i][j]))
            not_blank += 1
        elif office[i][j] == '6':
            not_blank += 1
dfs(0)
print(M * N - max_camera - not_blank)
