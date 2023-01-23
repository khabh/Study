import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, n + 1)])
result = []
for i in range(n - 1):
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
result.append(queue.popleft())
print(f'<{str(result)[1:-1]}>')

