import sys


def dfs(count, index):
    global answer, a, b
    if count > 0:
        answer = min(answer, abs(a - b))
    if count == N // 2:
        return
    for i in range(index + 1, N):
        if not visit[i]:
            temp_a, temp_b = a, b
            for j in range(N):
                if visit[j]:
                    temp_b += (score[i][j] + score[j][i])
                else:
                    temp_a -= (score[i][j] + score[j][i])
            visit[i] = True
            dfs(count + 1, i)
            visit[i] = False
            a, b = temp_a, temp_b


read = sys.stdin.readline
N = int(read())
score = [list(map(int, read().split())) for _ in range(N)]
a = sum(sum(x) for x in score)
b = 0
visit = [False] * N
answer = sys.maxsize
dfs(0, -1)
print(answer)
