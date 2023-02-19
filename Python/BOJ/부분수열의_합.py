import sys


def dfs(hap, index):
    if index == N:
        return
    result.add(hap + s[index])
    dfs(s[index] + hap, index + 1)
    dfs(hap, index + 1)


read = sys.stdin.readline
N = int(read())
s = list(map(int, read().split()))
result = set()
dfs(0, 0)
i = 1
while 1:
    if i not in result:
        print(i)
        break
    i += 1
