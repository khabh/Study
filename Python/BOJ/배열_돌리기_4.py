import sys
import copy


def rotate_graph(graph, index):
    r, c, s = rotate[index]
    r -= 1
    c -= 1
    for i in range(1, s + 1):
        cache = graph[r - i][c + i]
        for j in range(c + i, c - i, - 1):
            graph[r - i][j] = graph[r - i][j - 1]
        for j in range(r - i, r + i):
            graph[j][c - i] = graph[j + 1][c - i]
        for j in range(c - i, c + i):
            graph[r + i][j] = graph[r + i][j + 1]
        for j in range(r + i, r - i, -1):
            graph[j][c + i] = graph[j - 1][c + i]
        graph[r - i + 1][c + i] = cache
    return graph


def dfs(graph, count):
    global result
    if count == K:
        result = min(result, min(sum(x) for x in graph))
        return
    for i in range(K):
        if i not in visit:
            visit.add(i)
            dfs(rotate_graph(copy.deepcopy(graph), i), count + 1)
            visit.remove(i)


read = sys.stdin.readline
N, M, K = map(int, read().split())
A = [list(map(int, read().split())) for _ in range(N)]
rotate = [list(map(int, read().split())) for _ in range(K)]
visit = set()
result = sys.maxsize
dfs(A, 0)
print(result)
