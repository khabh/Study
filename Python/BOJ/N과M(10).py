import sys


def solve(index, count):
    if count == M:
        result.append(' '.join(map(str, answer)))
        return
    prev = 0
    for i in range(index + 1, N):
        if not visit[i] and numbers[i] != prev:
            visit[i] = True
            prev = numbers[i]
            answer.append(numbers[i])
            solve(i, count + 1)
            visit[i] = False
            answer.pop()


N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
answer = []
result = []
visit = [False] * N
solve(-1, 0)
print('\n'.join(result))
