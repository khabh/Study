import sys


def solve(count):
    if count == M:
        result.append(' '.join(map(str, answer)))
        return
    for i, number in enumerate(numbers):
        if not visit[i]:
            visit[i] = True
            answer.append(number)
            solve(count + 1)
            answer.pop()
            visit[i] = False


N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
visit = [False] * N
answer = []
result = []
for i, number in enumerate(numbers):
    answer.append(number)
    visit[i] = True
    solve(1)
    visit[i] = False
    answer.pop()
print('\n'.join(result))
