import sys

read = sys.stdin.readline
N = int(read())
ranks = [0] + sorted([int(read()) for _ in range(N)])
result = 0
for i in range(1, N + 1):
    result += abs(ranks[i] - i)
print(result)
