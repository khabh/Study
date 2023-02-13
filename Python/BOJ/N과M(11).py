import sys


def solve(index, count):
    if count == M:
        result.append(' '.join(map(str, answer)))
        return
    prev = 0
    for i in range(index, N):
        if numbers[i] != prev:
            prev = numbers[i]
            answer.append(numbers[i])
            solve(i, count + 1)
            answer.pop()


N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
answer = []
result = []
solve(0, 0)
print('\n'.join(result))
