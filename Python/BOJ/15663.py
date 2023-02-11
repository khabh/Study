import sys


def solve(count):
    if count == M:
        result.append(' '.join(map(str, answer)))
        return
    prev = 0
    for i in range(N):
        if not visit[i] and numbers[i] != prev:
            visit[i] = True
            prev = numbers[i]
            answer.append(numbers[i])
            solve(count + 1)
            visit[i] = False
            answer.pop()


N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
answer = []
result = []
visit = [False] * N
solve(0)
# for i, number in enumerate(numbers):
#     visit[i] = True
#     answer.append(number)
#     solve(1)
#     visit[i] = False
#     answer.pop()
print('\n'.join(result))
