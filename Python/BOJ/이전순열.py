import sys


def solve():
    for i in range(N - 2, -1, -1):
        if numbers[i] > numbers[i + 1]:
            for j in range(N - 1, i - 1, -1):
                if numbers[j] < numbers[i]:
                    numbers[j], numbers[i] = numbers[i], numbers[j]
                    return ' '.join(map(str, numbers[:i + 1] + sorted(numbers[i + 1:], reverse=True)))
    return '-1'


read = sys.stdin.readline
N = int(read())
numbers = list(map(int, read().split()))
print(solve())