import sys
import heapq

read = sys.stdin.readline
N = int(read())
problems = []
result = []
for _ in range(N):
    deadline, count = map(int, read().split())
    heapq.heappush(problems, (deadline, count))
for _ in range(N):
    deadline, count = heapq.heappop(problems)
    heapq.heappush(result, count)
    if len(result) > deadline:
        heapq.heappop(result)
print(sum(result))
