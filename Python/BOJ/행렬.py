import sys


def flip(x, y):
    for a in range(x, x + 3):
        for b in range(y, y + 3):
            if A[a][b] == '0':
                A[a][b] = '1'
            else:
                A[a][b] = '0'


read = sys.stdin.readline
N, M = map(int, read().split())
A = [list(read().rstrip()) for _ in range(N)]
B = [list(read().rstrip()) for _ in range(N)]
count = 0
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            count += 1
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            count = -1
            break
    if count == -1:
        break
print(count)