import sys


def gcd(x, y):
    while x > 0:
        x, y = y % x, x
    return y


a, b = map(int, sys.stdin.readline().split())
print('1' * gcd(min(a, b), max(a, b)))
