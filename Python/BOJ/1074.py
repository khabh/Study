import sys


def solved(block_size, x, y):
    global result
    if x == r and y == c:
        print(result)
        sys.exit()

    if block_size == 1:
        result += 1
        return

    if not (x <= r < x + block_size and y <= c < y + block_size):
        result += block_size ** 2
        return

    next = block_size // 2
    solved(next, x, y)
    solved(next, x + next, y)
    solved(next, x, y + next)
    solved(next, x + next, y + next)


N, r, c = map(int, sys.stdin.readline().rstrip().split())
result = 0
solved(2 ** N, 0, 0)
