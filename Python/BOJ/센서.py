import sys
import heapq

read = sys.stdin.readline
N = int(read())
K = int(read())
s = sorted(list(map(int, read().split())))
result = s[-1] - s[0]
distance = []
for i in range(1, N):
    heapq.heappush(distance, s[i - 1] - s[i])
for _ in range(K - 1):
    if not len(distance):
        break
    result += heapq.heappop(distance)
print(result)
