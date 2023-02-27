import sys

N, M, K = map(int, sys.stdin.readline().split())
result = min(N // 2, M)
remain = N + M - 3 * result
while remain < K:
    result -= 1
    remain += 3
print(result)
