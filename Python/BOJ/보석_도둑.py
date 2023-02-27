import sys
import heapq

read = sys.stdin.readline
N, K = map(int, read().split())
gem = []
for _ in range(N):
    m, v = map(int, read().split())
    gem.append((m, v))
bags = sorted(list(int(read()) for _ in range(K)))
gem.sort(key=lambda x: -x[0])
result = 0
light_gem = []
for bag in bags:
    while gem and bag >= gem[-1][0]:
        heapq.heappush(light_gem, -gem.pop()[1])
    if light_gem:
        result -= heapq.heappop(light_gem)
print(result)
