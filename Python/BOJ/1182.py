import sys


def dfs(index, result, cnt):
    global count
    if result == S and cnt > 0:
        count += 1
    for i in range(index, N):
        result += numbers[i]
        dfs(i + 1, result, cnt + 1)
        result -= numbers[i]


read = sys.stdin.readline
N, S = map(int, read().split())
numbers = list(map(int, read().split()))
count = 0
dfs(0, 0, 0)
print(count)