import sys
from collections import deque


def bfs():
    visit = set()
    visit.add(A)
    queue = deque([(A, '')])
    while 1:
        n, path = queue.popleft()
        if n == B:
            print(path)
            return
        D = (n * 2) % 10000
        if D not in visit:
            visit.add(D)
            queue.append((D, path + 'D'))
        L = (10 * n + (n // 1000)) % 10000
        if L not in visit:
            visit.add(L)
            queue.append((L, path + 'L'))
        R = (n // 10) + (n % 10) * 1000
        if R not in visit:
            visit.add(R)
            queue.append((R, path + 'R'))
        S = (n - 1) % 10000
        if S not in visit:
            visit.add(S)
            queue.append((S, path + 'S'))


read = sys.stdin.readline
for _ in range(int(read())):
    A, B = map(int, read().split())
    bfs()
