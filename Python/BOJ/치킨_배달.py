import sys


def calc_distance(visit):
    global result
    total = 0
    for site in house:
        min_distance = 500
        for chicken in visit:
            min_distance = min(min_distance, house[site][chicken])
        total += min_distance
    result = min(result, total)


def dfs(visit, index):
    if len(visit) == M:
        calc_distance(visit)
        return
    if index == len(chickens):
        return
    visit.append(chickens[index])
    dfs(visit, index + 1)
    visit.pop()
    dfs(visit, index + 1)


read = sys.stdin.readline
N, M = map(int, read().split())
city = [read().split() for _ in range(N)]
chickens = []
house = {}
result = sys.maxsize
for i in range(N):
    for j in range(N):
        if city[i][j] == '0':
            continue
        if city[i][j] == '1':
            house[(i, j)] = {}
        else:
            chickens.append((i, j))
for x1, y1 in house:
    for x2, y2 in chickens:
        house[(x1, y1)][(x2, y2)] = abs(x1 - x2) + abs(y1 - y2)
dfs([], 0)
print(result)
