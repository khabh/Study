import sys

read = sys.stdin.readline
N, C = map(int, read().split())
house = list(int(read()) for _ in range(N))
house.sort()
start = 1
end = int((house[-1] - house[0]) / (C - 1))
while start <= end:
    mid = (start + end) // 2
    count = 1
    dist = house[0]
    for h in house[1:]:
        if h >= dist + mid:
            count += 1
            dist = h
        if count >= C:
            break
    if count < C:
        end = mid - 1
    else:
        start = mid + 1
print(end)
