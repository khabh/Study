import sys


def all_match():
    for i in range(1, N + 1):
        site = i
        for j in range(1, H + 1):
            site = ladder[j].get(site, site)
        if site != i:
            return False
    return True


def dfs(index, count):
    global result
    if count >= result:
        return
    if all_match():
        result = min(result, count)
        return
    if count == 3 or index == len(no_cross):
        return
    dfs(index + 1, count)
    x, y = no_cross[index]
    if x not in ladder[y] and x + 1 not in ladder[y]:
        ladder[y][x] = x + 1
        ladder[y][x + 1] = x
        dfs(index + 1, count + 1)
        del ladder[y][x]
        del ladder[y][x + 1]


read = sys.stdin.readline
N, M, H = map(int, read().split())
ladder = [{} for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, read().split())
    ladder[a][b] = b + 1
    ladder[a][b + 1] = b
result = 4
no_cross = []
for a in range(1, N):
    for b in range(1, H + 1):
        if a not in ladder[b] and a + 1 not in ladder[b]:
            no_cross.append((a, b))
dfs(0, 0)
if result == 4:
    print('-1')
else:
    print(result)
