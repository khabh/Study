import sys


def check(n):
    global min_count
    length = len(str(n))
    for i in range(length):
        digit = (n // 10 ** i) % 10
        if digit in broken:
            return

    result = abs(n - target) + length
    if min_count > result:
        min_count = result


input = sys.stdin.readline
target = int(input())
N = int(input())
broken = set(map(int, input().split()))
min_count = abs(100 - target)

for num in range(1000001):
    check(num)
print(min_count)

