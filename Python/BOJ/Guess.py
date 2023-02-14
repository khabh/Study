import sys


def check(index):
    hap = answer[index]
    for i in range(index + 1, N):
        hap += answer[i]
        if (hap > 0 and sign[index][i] != 1) or (hap < 0 and sign[index][i] != -1) or (hap == 0 and sign[index][i] != 0):
            return False
    return True


def dfs(index):
    if index == -1:
        print(' '.join(map(str, answer)))
        sys.exit()
    if not sign[index][index]:
        answer[index] = 0
        if check(index):
            dfs(index - 1)
        return
    for i in range(1, 11):
        answer[index] = i * sign[index][index]
        if check(index):
            dfs(index - 1)


read = sys.stdin.readline
N = int(read())
matrix = read()
answer = [0] * N
n = 0
sign = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        if matrix[n] == '+':
            sign[i][j] = 1
        elif matrix[n] == '-':
            sign[i][j] = -1
        n += 1
dfs(N - 1)