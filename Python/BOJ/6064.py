import sys
import math


def solve():
    m, n, x, y = map(int, read().split())
    max_value = math.lcm(m, n)
    while x <= max_value:
        if (x - y) % n == 0:
            print(x)
            return
        x += m
    print('-1')


read = sys.stdin.readline
for i in range(int(read())):
    solve()
