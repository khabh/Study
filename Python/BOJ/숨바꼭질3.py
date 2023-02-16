import sys
from collections import deque


def bfs():
    visit = set()
    visit.add(N)
    queue = deque([(N, 0)])
    while 1:
        n, count = queue.popleft()
        next_n = 2 * n
        if next_n <= 100000 and next_n not in visit:
            if next_n == K:
                return count
            visit.add(next_n)
            queue.appendleft((next_n, count))
        next_n = n - 1
        if next_n >= 0 and next_n not in visit:
            if next_n == K:
                return count + 1
            visit.add(next_n)
            queue.append((next_n, count + 1))
        next_n = n + 1
        if next_n <= 100000 and next_n not in visit:
            if next_n == K:
                return count + 1
            visit.add(next_n)
            queue.append((next_n, count + 1))


N, K = map(int, sys.stdin.readline().split())
if N == K:
    print('0')
else:
    print(bfs())
