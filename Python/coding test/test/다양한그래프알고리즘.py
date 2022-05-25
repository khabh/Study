def find_parent(x, parent):
    if parent[x] != x:
        return find_parent(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b, parent)

for i in range(1, n+1):
    print(find_parent(i, parent), end=' ')

print()
print(*parent)
