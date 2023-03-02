import sys
import heapq

read = sys.stdin.readline
N, M = map(int, read().split())
plus = [0]
minus = [0]
for book in map(int, read().split()):
    if book > 0:
        heapq.heappush(plus, -book)
    else:
        heapq.heappush(minus, book)
result = min(plus[0], minus[0])
for _ in range((len(plus) - 1) // M):
    result -= (heapq.heappop(plus) * 2)
    for i in range(M - 1):
        heapq.heappop(plus)
if len(plus) > 1:
    result -= (plus[0] * 2)
for _ in range((len(minus) - 1) // M):
    result -= (heapq.heappop(minus) * 2)
    for i in range(M - 1):
        heapq.heappop(minus)
if len(minus) > 1:
    result -= (minus[0] * 2)
print(result)
