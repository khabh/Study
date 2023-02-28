import sys
sys.setrecursionlimit(10 ** 6)


def dfs(gap, index, count):
    global result
    if index == N:
        result = min(result, count)
        return
    if gap == NO_GAP:
        gap = numbers[index] - numbers[index - 1]
        numbers[index] += 1
        dfs(gap + 1, index + 1, count + 1)
        numbers[index] -= 2
        dfs(gap -1, index + 1, count + 1)
        numbers[index] += 1
        dfs(gap, index + 1, count)
        return
    current_gap = numbers[index] - numbers[index - 1]
    if gap == current_gap:
        dfs(gap, index + 1, count)
    elif gap == current_gap + 1:
        numbers[index] += 1
        dfs(gap, index + 1, count + 1)
        numbers[index] -= 1
    elif gap == current_gap - 1:
        numbers[index] -= 1
        dfs(gap, index + 1, count + 1)
        numbers[index] += 1


read = sys.stdin.readline
N = int(read())
result = 10 ** 5 + 1
NO_GAP = 10 ** 10
numbers = list(map(int, read().split()))
dfs(NO_GAP, 1, 0)
numbers[0] -= 1
dfs(NO_GAP, 1, 1)
numbers[0] += 2
dfs(NO_GAP, 1, 1)
if result == 10 ** 5 + 1:
    print('-1')
else:
    print(result)
