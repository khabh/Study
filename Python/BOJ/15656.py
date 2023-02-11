import sys


def solve(count):
    if count == M:
        result.append(' '.join(map(str, answer)))
        return
    for number in numbers:
        answer.append(number)
        solve(count + 1)
        answer.pop()


N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
answer = []
result = []
for number in numbers:
    answer.append(number)
    solve(1)
    answer.pop()
print('\n'.join(result))
