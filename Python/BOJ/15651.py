import sys


def solve(count):
    if count == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N + 1):
        answer.append(i)
        solve(count + 1)
        answer.pop()


N, M = map(int, sys.stdin.readline().split())
answer = []
for i in range(1, N + 1):
    answer.append(i)
    solve(1)
    answer.pop()
