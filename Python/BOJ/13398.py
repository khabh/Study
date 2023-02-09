import sys

read = sys.stdin.readline
N = int(read())
numbers = list(map(int, read().split()))
first_dp = numbers[:]
for i in range(1, N):
    if first_dp[i - 1] > 0:
        first_dp[i] += first_dp[i - 1]
if N < 3:
    print(max(first_dp))
    sys.exit()
second_dp = first_dp[:]
second_dp[2] = first_dp[0] + numbers[2]
for i in range(3, N):
    second_dp[i] = max(second_dp[i - 1], first_dp[i - 2]) + numbers[i]
print(max(max(first_dp), max(second_dp)))
