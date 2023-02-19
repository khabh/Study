import sys


def dfs(energy, count):
    global result
    if count == N - 2:
        result = max(result, energy)
        return
    for i in range(1, N - 1):
        if visit[i]:
            continue
        new_energy = 1
        for j in range(i - 1, -1, -1):
            if not visit[j]:
                new_energy *= marbles[j]
                break
        for j in range(i + 1, N):
            if not visit[j]:
                new_energy *= marbles[j]
                break
        visit[i] = True
        dfs(energy + new_energy, count + 1)
        visit[i] = False


read = sys.stdin.readline
N = int(read())
marbles = list(map(int, read().split()))
visit = [False] * N
result = 0
dfs(0, 0)
print(result)
