import sys


def solve(number, count):
    if count == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(number, N + 1):
        answer.append(i)
        solve(i, count + 1)
        answer.pop()


N, M = map(int, sys.stdin.readline().split())
visit = [False] * (N + 1)
answer = []
for i in range(1, N + 1):
    answer.append(i)
    solve(i, 1)
    answer.pop()
