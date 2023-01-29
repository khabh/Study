import sys


def move(n, s, e):
    if n == 1:
        print(s, e)
        return
    move(n - 1, s, 6 - s - e)
    print(s, e)
    move(n - 1, 6 - s - e, e)


K = int(sys.stdin.readline())
print(2 ** K - 1)
move(K, 1, 3)

