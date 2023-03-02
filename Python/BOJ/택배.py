import sys

read = sys.stdin.readline
N, C = map(int, read().split())
boxes = [[] for _ in range(N + 1)]
weight = 0
load = [0] * (N + 1)
result = 0
for i in range(int(read())):
    a, b, c = map(int, read().split())
    boxes[a].append((b, c))
for i in range(1, N + 1):
    if load[i]:
        result += load[i]
        weight -= load[i]
    for end, box in boxes[i]:
        load[end] += box
        weight += box
    index = N
    while index > i and weight > C:
        out = min(load[index], weight - C)
        load[index] -= out
        weight -= out
        index -= 1
print(result)

