import sys
from collections import deque


def bfs():
    visit = {(0, 0, C): 0}
    queue = deque([(0, 0, C)])
    while queue:
        a, b, c = queue.popleft()
        if a == 0:
            result.add(c)
        if a > 0:
            if B > b:
                change = min(a, B - b)
                bottle = (a - change, b + change, c)
                if bottle not in visit:
                    visit[bottle] = 0
                    queue.append(bottle)
            if C > c:
                change = min(a, C - c)
                bottle = (a - change, b, c + change)
                if bottle not in visit:
                    visit[bottle] = 0
                    queue.append(bottle)
        if b > 0:
            if A > a:
                change = min(b, A - a)
                bottle = (a + change, b - change, c)
                if bottle not in visit:
                    visit[bottle] = 0
                    queue.append(bottle)
            if C > c:
                change = min(b, C - c)
                bottle = (a, b - change, c + change)
                if bottle not in visit:
                    visit[bottle] = 0
                    queue.append(bottle)
        if c > 0:
            if B > b:
                change = min(c, B - b)
                bottle = (a, b + change, c - change)
                if bottle not in visit:
                    visit[bottle] = 0
                    queue.append(bottle)
            if A > a:
                change = min(c, A - a)
                bottle = (a + change, b, c - change)
                if bottle not in visit:
                    visit[bottle] = 0
                    queue.append(bottle)



A, B, C = map(int, sys.stdin.readline().split())
result = set()
bfs()
print(*sorted(result), sep=' ')