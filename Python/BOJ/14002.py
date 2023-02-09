import sys
from collections import deque

read = sys.stdin.readline
A = int(read())
numbers = list(map(int, read().split()))
dp = [1] * A
dpPrev = [-1] * A
for i in range(1, A):
    current_max = (-1, dp[i])
    for j in range(i):
        if numbers[j] < numbers[i] and dp[j] + 1 > current_max[1]:
            current_max = (j, dp[j] + 1)
    dpPrev[i], dp[i] = current_max
max_index = dp.index(max(dp))
print(dp[max_index])
result = deque()
while max_index != -1:
    result.appendleft(str(numbers[max_index]))
    max_index = dpPrev[max_index]
print(' '.join(result))

