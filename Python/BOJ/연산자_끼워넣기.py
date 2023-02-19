import sys


def dfs(value, index):
    global max_value, min_value
    if index == N:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return
    if sign[0]:
        sign[0] -= 1
        dfs(value + numbers[index], index + 1)
        sign[0] += 1
    if sign[1]:
        sign[1] -= 1
        dfs(value - numbers[index], index + 1)
        sign[1] += 1
    if sign[2]:
        sign[2] -= 1
        dfs(value * numbers[index], index + 1)
        sign[2] += 1
    if sign[3]:
        sign[3] -= 1
        dfs(int(value / numbers[index]), index + 1)
        sign[3] += 1


read = sys.stdin.readline
N = int(read())
numbers = list(map(int, read().split()))
sign = list(map(int, read().split()))
max_value = -1e9
min_value = sys.maxsize
dfs(numbers[0], 1)
print(max_value)
print(min_value)
