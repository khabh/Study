import sys
from collections import Counter

read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
tree = Counter(map(int, read().split()))
e = 1000000000
s = 0
while s <= e:
    mid = (s + e) // 2
    if sum((h - mid) * i for h, i in tree.items() if h > mid) >= M:
        s = mid + 1
    else:
        e = mid - 1
print(e)
