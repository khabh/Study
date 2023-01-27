import sys

read = sys.stdin.readline
N, C = map(int, read().rstrip().split())
h = [int(read()) for _ in range(N)]
h.sort()

s = 1
e = (h[-1] - h[0]) // (C - 1) + 1
while s <= e:
    mid = (s + e) // 2
    count = 1
    dist = h[0]
    for d in h:
        if d >= dist + mid:
            count += 1
            dist = d
        if count >= C:
            break
    if count >= C:
        s = mid + 1
    else:
        e = mid - 1
print(e)
