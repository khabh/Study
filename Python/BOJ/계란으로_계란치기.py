import sys


def dfs(index, count):
    global result
    if index == N or count == N or (eggs[index] > 0 and count == N - 1):
        result = max(result, count)
        return
    if eggs[index] <= 0:
        dfs(index + 1, count)
        return

    for i in range(N):
        if i != index and eggs[i] > 0:
            eggs[index] -= weights[i]
            eggs[i] -= weights[index]
            temp = 0
            if eggs[index] <= 0:
                temp += 1
            if eggs[i] <= 0:
                temp += 1
            dfs(index + 1, count + temp)
            if result == N:
                return
            eggs[index] += weights[i]
            eggs[i] += weights[index]


read = sys.stdin.readline
N = int(read())
eggs = []
weights = []
for _ in range(N):
    egg, weight = map(int, read().split())
    eggs.append(egg)
    weights.append(weight)
result = 0
dfs(0, 0)
print(result)