import sys


def dfs(x, y):
    if y == c - 1:
        return True
    y += 1
    for i in range(x - 1, x + 2):
        if 0 <= i < r and graph[i][y] == '.' and (i, y) not in visit:
            visit.add((i, y))
            if dfs(i, y):
                return True


read = sys.stdin.readline
r, c = map(int, read().split())
graph = [read().rstrip() for _ in range(r)]
visit = set()
result = 0
for j in range(r):
    if dfs(j, 0):
        result += 1
print(result)
