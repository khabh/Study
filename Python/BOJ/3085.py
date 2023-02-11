import sys


def count_row(a, b):
    global max_count
    for x in range(a, b):
        count = 1
        prev = candy[x][0]
        for n in candy[x][1:]:
            if n == prev:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
                prev = n
        max_count = max(count, max_count)


def count_column(a, b):
    global max_count
    for y in range(a, b):
        count = 1
        prev = candy[0][y]
        for x in range(1, N):
            if candy[x][y] == prev:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
                prev = candy[x][y]
        max_count = max(count, max_count)


read = sys.stdin.readline
max_count = 0
N = int(read())
candy = [list(read().rstrip()) for _ in range(N)]
count_row(0, N)
count_column(0, N)

for i in range(N):
    for j in range(N):
        if i + 1 < N and candy[i][j] != candy[i + 1][j]:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            count_row(i, i + 2)
            count_column(j, j + 1)
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
        if j + 1 < N and candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            count_row(i, i + 1)
            count_column(j, j + 2)
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        if max_count == N:
            print(N)
            sys.exit()
print(max_count)
