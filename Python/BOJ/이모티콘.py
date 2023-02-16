import sys
from collections import deque


def bfs():
    visit = set()
    visit.add((1, 0))
    queue = deque([(1, 0, 0)])
    while 1:
        n, clipboard, count = queue.popleft()
        next_count = clipboard + n
        if next_count <= 1000 and (next_count, clipboard) not in visit:
            if next_count == S:
                return count + 1
            visit.add((next_count, clipboard))
            queue.append((next_count, clipboard, count + 1))
        next_count = n - 1
        if next_count >= 2 and (next_count, clipboard) not in visit:
            if next_count == S:
                return count + 1
            visit.add((next_count, clipboard))
            queue.append((next_count, clipboard, count + 1))
        if (n, n) not in visit:
            visit.add((n, n))
            queue.append((n, n, count + 1))


S = int(sys.stdin.readline())
print(bfs())
