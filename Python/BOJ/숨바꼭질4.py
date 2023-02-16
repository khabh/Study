import sys
from collections import deque


def bfs(find):
    visit = {N: - 1}
    queue = deque([(N, 0)])
    while find not in visit:
        n, count = queue.popleft()
        if n - 1 >= 0 and (n - 1) not in visit:
            visit[n - 1] = n
            queue.append((n - 1, count + 1))
        if n + 1 <= 100000 and (n + 1) not in visit:
            visit[n + 1] = n
            queue.append((n + 1, count + 1))
        if n * 2 <= 100000 and (n * 2) not in visit:
            visit[n * 2] = n
            queue.append((n * 2, count + 1))
    result = deque([])
    while find != -1:
        result.appendleft(find)
        find = visit[find]
    return result


N, K = map(int, sys.stdin.readline().split())
answer = bfs(K)
print(len(answer) - 1)
print(' '.join(map(str, answer)))
