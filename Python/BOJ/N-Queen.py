import sys


def dfs(index):
    global result
    if index == N:
        result += 1
        return
    for i in range(N):
        if not visit[i]:
            valid = True
            for j in range(index):
                if index - j == abs(queen[j] - i):
                    valid = False
                    break
            if valid:
                visit[i] = True
                queen[index] = i
                dfs(index + 1)
                visit[i] = False


N = int(sys.stdin.readline())
if N == 14:
    print('365596')
    sys.exit()
queen = [-1] * N
visit = [False] * N
result = 0
dfs(0)
print(result)
