import sys


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    while b > 0:
        a, b = b, a % b

    return a


for _ in range(int(sys.stdin.readline())):
    n = list(map(int, sys.stdin.readline().split()))
    result = 0
    for i in range(1, n[0]):
        for j in range(i + 1, n[0] + 1):
            result += gcd(n[i], n[j])
    print(result)
