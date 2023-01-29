import sys


def compress(size, x, y):
    a = image[x][y]
    valid = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if image[i][j] != a:
                valid = False
                break
        if not valid:
            break

    if valid:
        return a
    if size == 2:
        result = [image[x][y], image[x][y + 1], image[x + 1][y], image[x + 1][y + 1]]
        return f'({"".join(result)})'

    next_size = size // 2
    result = []
    for i in range(x, x + size, next_size):
        for j in range(y, y + size, next_size):
            result.append(compress(next_size, i, j))
    return f'({"".join(result)})'


read = sys.stdin.readline
N = int(read())
image = [read() for _ in range(N)]
print(compress(N, 0, 0))
