import sys


def count_paper(size, x, y):
    global count
    start = paper[x][y]
    is_paper = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != start:
                is_paper = False
                break
        if not is_paper:
            break

    if is_paper:
        count[start] += 1
        return

    if size == 3:
        for i in range(x, x + size):
            for j in range(y, y + size):
                count[paper[i][j]] += 1
        return

    else:
        next_size = size // 3
        for i in range(x, x + size, next_size):
            for j in range(y, y + size, next_size):
                count_paper(next_size, i, j)


read = sys.stdin.readline
N = int(read())
paper = [list(read().split()) for _ in range(N)]
count = {'1': 0, '-1': 0, '0': 0}
if N == 1:
    count[paper[0][0]] = 1
else:
    count_paper(N, 0, 0)
print(count['-1'])
print(count['0'])
print(count['1'])
