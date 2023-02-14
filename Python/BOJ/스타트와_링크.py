import sys


def dfs(count, index):
    global answer
    if count == N // 2:
        a = b = 0
        for i in range(N):
            for j in range(N):
                if visit[i] and visit[j]:
                    a += score[i][j]
                elif not visit[i] and not visit[j]:
                    b += score[i][j]
        answer = min(answer, abs(a - b))
        return
    for i in range(index + 1, N):
        if not visit[i]:
            visit[i] = True
            dfs(count + 1, i)
            visit[i] = False


read = sys.stdin.readline
N = int(read())
score = [list(map(int, read().split())) for _ in range(N)]
visit = [True] + [False] * (N - 1)
answer = sys.maxsize
dfs(1, 0)
print(answer)
