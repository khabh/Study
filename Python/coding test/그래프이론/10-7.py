

def find_parent(student, x):
    if student[x] != x:
        student[x] = find_parent(student, student[x])
    return student[x]


def union(student, a, b):
    a = find_parent(student, a)
    b = find_parent(student, b)
    if a < b:
        student[b] = a
    else:
        student[a] = b


n, m = map(int, input().split())
student = [0]*(n+1)

for i in range(1, n+1):
    student[i] = i

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(student, a, b)
    else:
        if find_parent(student, a) == find_parent(student, b):
            print("YES")
        else:
            print("NO")
