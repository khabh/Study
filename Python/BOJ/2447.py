import sys


def get_star(size, x, y):
    if size == 3:
        star[x + 1][y + 1] = ' '
        return

    next_size = size // 3
    for i in range(x + next_size, x + next_size * 2):
        for j in range(y + next_size, y + next_size * 2):
            star[i][j] = ' '

    next_size = size // 3
    skipX = x + next_size
    skipY = y + next_size
    for i in range(x, x + size, next_size):
        for j in range(y, y + size, next_size):
            if i == skipX and j == skipY:
                continue
            get_star(next_size, i, j)


N = int(sys.stdin.readline())
star = [['*'] * N for _ in range(N)]
get_star(N, 0, 0)
for i in range(len(star)):
    star[i] = ''.join(star[i])
print('\n'.join(star))
