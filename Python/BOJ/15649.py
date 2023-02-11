import sys


def solve(count):
    if count == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N + 1):
        if not visit[i]:
            visit[i] = True
            answer.append(i)
            solve(count + 1)
            visit[i] = False
            answer.pop()


N, M = map(int, sys.stdin.readline().split())
visit = [False] * (N + 1)
answer = []
for i in range(1, N + 1):
    answer.append(i)
    visit[i] = True
    solve(1)
    visit[i] = False
    answer.pop()
