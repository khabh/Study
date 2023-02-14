import sys

read = sys.stdin.readline
n, m = map(int, read().split())
paper = [list(map(int, read().rstrip())) for _ in range(n)]
ans = 0

for i in range(1 << n*m):
    total = 0
    for x in range(n):
        row_sum = 0
        for y in range(m):
            idx = x * m + y
            if i & (1 << idx) != 0:
                row_sum = row_sum * 10 + paper[x][y]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    for y in range(m):
        col_sum = 0
        for x in range(n):
            idx = x * m + y
            if i & (1 << idx) == 0:
                col_sum = col_sum * 10 + paper[x][y]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
    ans = max(ans, total)

print(ans)