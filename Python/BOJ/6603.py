import sys
from collections import deque


def dfs(index, count):
    if count == 6:
        result.append(' '.join(answer))
        return
    for i in range(index, K - 5 + count):
        answer.append(n[i])
        dfs(i + 1, count + 1)
        answer.pop()


read = sys.stdin.readline
while True:
    n = read().rstrip()
    if n == '0':
        break
    result = deque()
    n = sorted(n.split()[1:], key=int)
    K = len(n)
    answer = deque()
    dfs(0, 0)
    print('\n'.join(result))
    print()
