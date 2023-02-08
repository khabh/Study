import sys
from collections import Counter


def solve(a, b):
    count = 0
    for number in a:
        count += a[number] * b[-number]
    print(count)


read = sys.stdin.readline
numbers = [list(map(int, read().split())) for _ in range(int(read()))]
first = Counter()
second = Counter()
for i in range(len(numbers)):
    for j in range(len(numbers)):
        first[numbers[i][0] + numbers[j][1]] += 1
        second[numbers[i][2] + numbers[j][3]] += 1
if len(first) > len(second):
    solve(second, first)
else:
    solve(first, second)
