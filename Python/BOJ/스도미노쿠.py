import sys
read = sys.stdin.readline


def valid_row(x, y, a, b):
    for i in range(9):
        if sudoku[i][y] == a or sudoku[i][y + 1] == b or sudoku[x][i] == a or sudoku[x][i] == b:
            return False
    return True


def valid_column(x, y, a, b):
    for i in range(9):
        if sudoku[i][y] == a or sudoku[i][y] == b or sudoku[x][i] == a or sudoku[x + 1][i] == b:
            return False
    return True


def valid_square(x, y, a):
    x, y = x // 3 * 3, y // 3 * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if sudoku[i][j] == a:
                return False
    return True


def dfs(index, count):
    if index == len(not_visit):
        return True
    x, y = not_visit[index]
    if sudoku[x][y]:
        return dfs(index + 1, count)
    for a, b in not_used:
        if (a, b) in visit:
            continue
        if y < 8 and not sudoku[x][y + 1]:
            if valid_row(x, y, a, b) and valid_square(x, y, a) and valid_square(x, y + 1, b):
                visit.add((a, b))
                sudoku[x][y], sudoku[x][y + 1] = a, b
                if dfs(index + 1, count + 2):
                    return True
                sudoku[x][y] = sudoku[x][y + 1] = 0
                visit.remove((a, b))
            if valid_row(x, y, b, a) and valid_square(x, y, b) and valid_square(x, y + 1, a):
                visit.add((a, b))
                sudoku[x][y], sudoku[x][y + 1] = b, a
                if dfs(index + 1, count + 2):
                    return True
                sudoku[x][y] = sudoku[x][y + 1] = 0
                visit.remove((a, b))
        if x < 8 and not sudoku[x + 1][y]:
            if valid_column(x, y, a, b) and valid_square(x, y, a) and valid_square(x + 1, y, b):
                visit.add((a, b))
                sudoku[x][y], sudoku[x + 1][y] = a, b
                if dfs(index + 1, count + 2):
                    return True
                sudoku[x][y] = sudoku[x + 1][y] = 0
                visit.remove((a, b))
            if valid_column(x, y, b, a) and valid_square(x, y, b) and valid_square(x + 1, y, a):
                visit.add((a, b))
                sudoku[x][y], sudoku[x + 1][y] = b, a
                if dfs(index + 1, count + 2):
                    return True
                sudoku[x + 1][y] = sudoku[x][y] = 0
                visit.remove((a, b))


cnt = 1
while 1:
    N = int(read())
    if not N:
        break
    print(f'Puzzle {cnt}')
    cnt += 1
    sudoku = [[0] * 9 for _ in range(9)]
    visit = set()
    for _ in range(N):
        U, LU, V, LV = read().split()
        U, V = int(U), int(V)
        sudoku[ord(LU[0]) - 65][int(LU[1]) - 1] = U
        sudoku[ord(LV[0]) - 65][int(LV[1]) - 1] = V
        if U > V:
            visit.add((V, U))
        else:
            visit.add((U, V))
    for i, site in enumerate(read().split()):
        sudoku[ord(site[0]) - 65][int(site[1]) - 1] = i + 1
    not_used = []
    not_visit = []
    for i in range(1, 9):
        for j in range(i + 1, 10):
            if (i, j) not in visit:
                not_used.append((i, j))
    for i in range(9):
        for j in range(9):
            if not sudoku[i][j]:
                not_visit.append((i, j))
    dfs(0, 0)
    print('\n'.join(''.join(map(str, row)) for row in sudoku))
