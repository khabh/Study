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


n, m = map(int, input().split())  # 노드 와 간선 개수
cycle = False
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if find_parent(a, parent) == find_parent(b, parent):
        cycle = True
    else:
        union(a, b, parent)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
