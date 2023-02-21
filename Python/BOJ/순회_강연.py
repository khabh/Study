import sys
import heapq

read = sys.stdin.readline
n = int(read())
numbers = []
for _ in range(n):
    fee, day = map(int, read().split())
    numbers.append((fee, day))
numbers.sort(key=lambda x: x[1])
result = []
for fee, day in numbers:
    heapq.heappush(result, fee)
    if len(result) > day:
        heapq.heappop(result)
print(sum(result))
