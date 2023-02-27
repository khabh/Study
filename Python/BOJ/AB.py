import sys


def solve(n, k):
    a = n
    b = 0
    while a * b < k and a:
        b += 1
        a -= 1
    if a * b < k:
        return -1
    if not k:
        return 'A' * n
    remain = k - a * (b - 1)
    return 'A' * remain + 'B' + 'A' * (a - remain) + 'B' * (b - 1)


N, K = map(int, sys.stdin.readline().split())
print(solve(N, K))
