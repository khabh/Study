import sys
input = sys.stdin.readline


def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
graph = []
parent = [i for i in range(n+1)]
result = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))


graph.sort()

for i in graph:
    cost, a, b = i
    if find_parent(a, parent) != find_parent(b, parent):
        union(a, b, parent)
        result.append(cost)


result.sort()

print(sum(result[:-1]))
