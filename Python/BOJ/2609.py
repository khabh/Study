import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n, k = map(int, sys.stdin.readline().split())
gcd = gcd(max(n, k), min(n, k))
print(gcd)
print(n * k // gcd)