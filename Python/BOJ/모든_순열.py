import sys

def dfs(count):
    if count == N:
        result.append(' '.join(map(str, answer)))
        return
    for i in range(1, N + 1):
        if not visit[i]:
            answer.append(i)
            visit[i] = True
            dfs(count + 1)
            visit[i] = False
            answer.pop()


N = int(sys.stdin.readline())
visit = [False] * (N + 1)
answer = []
result = []
dfs(0)
print('\n'.join(result))
