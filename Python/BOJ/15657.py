import sys


def solve(index, count):
    if count == M:
        result.append(' '.join(map(str, answer)))
        return
    for i in range(index, N):
        answer.append(numbers[i])
        solve(i, count + 1)
        answer.pop()


N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
answer = []
result = []
for i, number in enumerate(numbers):
    answer.append(number)
    solve(i, 1)
    answer.pop()
print('\n'.join(result))
