import sys
from collections import deque


def bfs(start, target):
    max_b = start.count('B') - target.count('B')
    max_a = len(start) - len(target) - max_b
    queue = deque([(start, max_b, max_a)])
    while queue:
        value, b, a = queue.popleft()
        if b and value[0] == 'B':
            if len(value) - 1 == len(target):
                if value[1:][::-1] == target:
                    return '1'
            else:
                queue.append((value[1:][::-1], b - 1, a))
        if a and value[-1] == 'A':
            if len(value) - 1 == len(target):
                if value[:-1] == target:
                    return '1'
            else:
                queue.append((value[:-1], b, a - 1))
    return '0'


read = sys.stdin.readline
S = read().rstrip()
N = read().rstrip()
print(bfs(N, S))
