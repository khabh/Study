import sys

read = sys.stdin.readline
N, L, R, X = map(int, read().split())
problems = list(map(int, read().split()))
result = 0
for status in range(1 << N):
    count = 0
    level = 0
    min_level = sys.maxsize
    max_level = 0
    for j in range(N):
        if status & (1 << j):
            count += 1
            level += problems[j]
            if level > R:
                break
            if problems[j] > max_level:
                max_level = problems[j]
            if problems[j] < min_level:
                min_level = problems[j]
    if count > 1 and L <= level <= R and max_level - min_level >= X:
        result += 1
print(result)
