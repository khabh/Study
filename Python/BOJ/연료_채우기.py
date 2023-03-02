import sys
import heapq

read = sys.stdin.readline
N = int(read())
station = [tuple(map(int, read().split())) for _ in range(N)]
station.sort()
end, fuel = map(int, read().split())
station.append((end, 0))
gas = []
result = 0
for i in range(N + 1):
    if fuel < station[i][0]:
        while gas:
            fuel -= heapq.heappop(gas)
            result += 1
            if fuel >= station[i][0]:
                break
    if not gas and fuel < station[i][0]:
        result = -1
        break
    else:
        heapq.heappush(gas, -station[i][1])
print(result)
