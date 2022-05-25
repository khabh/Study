n, m = map(int, input().split())
parent = [i for i in range(0, n+1)]


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


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b, parent)
    else:
        if find_parent(a, parent) == find_parent(b, parent):
            print('YES')
        else:
            print('NO')
